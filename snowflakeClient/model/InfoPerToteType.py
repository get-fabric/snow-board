from pydantic import BaseModel
from snowflakeClient.model import ToteTypeEnum


class InfoPerToteType(BaseModel):
    toteType: ToteTypeEnum
    itemToDecant: int
    binsNeeded: int
    emptyBinsAvailable: int
