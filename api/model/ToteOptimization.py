from typing import Dict
from pydantic import BaseModel
from api.model import FreeToteByActionEnum
from api.model.ToteTypeEnum import ToteTypeEnum


class ToteOptimization(BaseModel):
    def __init__(self, tote_type_enum: ToteTypeEnum,free_by_action: Dict[FreeToteByActionEnum, int]):
        super().__init__()
        self.tote_type_enum = tote_type_enum
        self.free_by_action = free_by_action

    tote_type_enum: ToteTypeEnum
    free_by_action: Dict[FreeToteByActionEnum, int]
