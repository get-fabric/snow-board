from pydantic import BaseModel
from snowflakeClient.model import InfoPerToteType


class InboundResponse(BaseModel):
    invoices: int
    ToteTypesNumber: int
    overallLines: int
    itemsToDecant: [InfoPerToteType]
