from pydantic import BaseModel
from snowflakeClient.model import FreeToteByActionEnum
from typing import Dict
from snowflakeClient.model import QC
from snowflakeClient.model import ToteExtraction
from snowflakeClient.model import ToteOptimization


class OperationalTasksResponse(BaseModel):
    qc: QC
    toteExtraction: ToteExtraction
    totesCanBeOptimized: [ToteOptimization]

    class FreeUpBinTips(BaseModel):
        class ToteOptimization(BaseModel):
            toteType: int
            freeByAction: Dict[FreeToteByActionEnum, int]

        totesCanBeOptimized: [ToteOptimization]
