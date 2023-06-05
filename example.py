
from snowflakeClient.SnowflakeClient import SnowflakeClient
import pandas as pd
# Gets the version
with SnowflakeClient() as sfclient:
    df = sfclient.query("SELECT current_version()")
    print(df)