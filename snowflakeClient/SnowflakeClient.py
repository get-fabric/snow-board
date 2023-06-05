from pathlib import Path
from snowflakeClient.exceptions import *
import snowflake.connector
import toml
from typing import Dict
import pandas as pd



class SnowflakeClient():
    def __init__(self):
        self._sf_config = None
        self._client = None
        self._load_snowflake_credentials()
        self._load_snowflake_configurations()

    def query(self, query_string: str,
              n_results: int = None,
              timeout: int = None):  # TODO: fill return type
        with self._client.cursor() as cs:
            if timeout:
                cs.execute('begin')
            cs.execute(query_string, timeout=timeout)
            df = cs.fetch_pandas_all()
            # print(df)
            return cs.fetch_pandas_all() if n_results is None else cs.fetch_pandas_all(n_results)
            # return cs.fetchall() if n_results is None else cs.fetch_all(n_results)


    def _connect(self) -> None:
        credentials = self._load_snowflake_credentials()
        self._client = snowflake.connector.connect(
            user=credentials['username'],
            password=credentials['password'],
            account=self._sf_config['SF_ACCOUNT'],
            role=self._sf_config['ROLE'],
            warehouse=self._sf_config['WAREHOUSE'],
            database=self._sf_config['DATABASE'],
        )

    def _load_snowflake_configurations(self) -> None:
        path_config = Path(__file__).parent / './.config/snowflake_connection.toml'
        self._sf_config = toml.load(path_config)

    def _load_snowflake_credentials(self) -> Dict:
        path_credentials = Path(__file__).parent / './.config/snowflake_credentials.toml'
        credentials = toml.load(path_credentials)
        if any(value == '' for value in credentials.values()):
            raise SnowflakeCredentialsNotProvidedError()
        return credentials

    def __enter__(self):
        self._connect()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._client.close()
