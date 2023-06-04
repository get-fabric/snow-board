from pydantic import BaseModel
from snowflakeClient.model import ToteSummery


class TotesStatusResponse(BaseModel):
    TotesSummery: [ToteSummery]
