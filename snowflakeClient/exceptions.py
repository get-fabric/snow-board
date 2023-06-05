class SnowflakeCredentialsNotProvidedError(Exception):
    """raised when snowflakeClient credentials are not set properly.
    check .config/snowflake_credentials.toml"""
    pass