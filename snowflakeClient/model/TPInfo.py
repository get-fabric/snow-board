from snowflakeClient.model import TPStateEnum
from snowflakeClient.model import ToteTypeEnum
from typing import Optional


class TPInfo():
    id: str
    status: TPStateEnum
    toteType: Optional[ToteTypeEnum]
    toteHeight: Optional[int]
    # TODO what data should i hold here
    operator: str
    # TODO on what timeframe
    operator_iph: int
