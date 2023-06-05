from pydantic import BaseModel
from typing import Dict
from api.model import QC, FreeToteByActionEnum, ToteOptimization, ToteExtraction


class OperationalTasksResponse(BaseModel):
    qc: QC
    toteExtraction: ToteExtraction
    totesCanBeOptimized: [ToteOptimization]

    class FreeUpBinTips(BaseModel):
        class ToteOptimization(BaseModel):
            toteType: int
            freeByAction: Dict[FreeToteByActionEnum, int]

        totesCanBeOptimized: [ToteOptimization]
