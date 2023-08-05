from typing import Optional

from google.cloud import bigquery
from lineage.bigquery_query import BigQueryQuery
from lineage.query import Query
from lineage.query_context import QueryContext
from lineage.query_history import QueryHistory
from lineage.utils import get_logger
from datetime import datetime

logger = get_logger(__name__)


class BigQueryQueryHistory(QueryHistory):
    INFORMATION_SCHEMA_QUERY_HISTORY = """
    SELECT query, end_time, dml_statistics.inserted_row_count + dml_statistics.updated_row_count, statement_type, 
    user_email, destination_table, referenced_tables
           
    FROM region-{location}.INFORMATION_SCHEMA.JOBS_BY_PROJECT
    WHERE
         project_id = @project_id
         AND creation_time BETWEEN @start_time AND {creation_time_range_end_expr}
         AND end_time BETWEEN @start_time AND {end_time_range_end_expr}
         AND job_type = "QUERY"
         AND state = "DONE"
         AND error_result is NULL
         AND query NOT like '%JOBS_BY_PROJECT%'
    ORDER BY end_time
    """
    INFO_SCHEMA_END_TIME_UP_TO_CURRENT_TIMESTAMP = 'CURRENT_TIMESTAMP()'
    INFO_SCHEMA_END_TIME_UP_TO_PARAMETER = '@end_time'

    def __init__(self, con, profile_database_name: str, profile_schema_name: str,
                 should_export_query_history: bool = True, ignore_schema: bool = False) -> None:
        super().__init__(con, profile_database_name, profile_schema_name, should_export_query_history, ignore_schema)

    @classmethod
    def _build_history_query(cls, start_date: datetime, end_date: datetime, database_name: str, location: str) -> \
            (str, []):
        query_parameters = [bigquery.ScalarQueryParameter("project_id", "STRING", database_name),
                            bigquery.ScalarQueryParameter("start_time", "TIMESTAMP", start_date)]

        end_time_range_end_expr = cls.INFO_SCHEMA_END_TIME_UP_TO_CURRENT_TIMESTAMP
        creation_time_range_end_expr = cls.INFO_SCHEMA_END_TIME_UP_TO_CURRENT_TIMESTAMP
        if end_date is not None:
            query_parameters.append(bigquery.ScalarQueryParameter("end_time",
                                                                  "TIMESTAMP",
                                                                  cls._include_end_date(end_date)))
            end_time_range_end_expr = cls.INFO_SCHEMA_END_TIME_UP_TO_PARAMETER
            creation_time_range_end_expr = cls.INFO_SCHEMA_END_TIME_UP_TO_PARAMETER

        query = cls.INFORMATION_SCHEMA_QUERY_HISTORY.format(location=location,
                                                            creation_time_range_end_expr=
                                                            creation_time_range_end_expr,
                                                            end_time_range_end_expr=
                                                            end_time_range_end_expr)
        return query, query_parameters

    def _query_history_table(self, start_date: datetime, end_date: datetime) -> [Query]:
        database_name = self.get_database_name()
        schema_name = self.get_schema_name()
        logger.debug(f"Pulling BigQuery history from database - {database_name} and schema - {schema_name}")

        query_text, query_parameters = self._build_history_query(start_date, end_date, database_name,
                                                                 self._con.location)

        job_config = bigquery.QueryJobConfig(
            query_parameters=query_parameters
        )

        job = self._con.query(query_text, job_config=job_config)

        logger.debug("Finished executing bigquery jobs history query")

        queries = []
        rows = job.result()
        for row in rows:
            query_context = QueryContext(query_time=row[1],
                                         query_volume=row[2],
                                         query_type=row[3],
                                         user_name=row[4],
                                         destination_table=row[5],
                                         referenced_tables=row[6])

            query = BigQueryQuery(raw_query_text=row[0],
                                  query_context=query_context,
                                  profile_database_name=database_name,
                                  profile_schema_name=schema_name)

            queries.append(query)
            self._query_history_stats.update_stats(query_context)

        logger.debug("Finished fetching bigquery history job results")

        return queries

    def properties(self) -> dict:
        query_history_properties = {'platform_type': 'bigquery'}
        query_history_properties.update(self._query_history_stats.to_dict())
        return query_history_properties
