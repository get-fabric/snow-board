from typing import Dict
from pydantic import BaseModel
from snowflakeClient.model import FreeToteByActionEnum


class ToteOptimization(BaseModel):
    toteType: int
    freeByAction: Dict[FreeToteByActionEnum, int]
