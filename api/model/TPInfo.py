from api.model import TPStateEnum
from api.model import ToteTypeEnum
from typing import Optional


class TPInfo:

    def __init__(self, id: str, status: TPStateEnum, tote_type: Optional[ToteTypeEnum], tote_height: Optional[int],
                 operator: str, operator_iph: int):
        super().__init__()
        self.id = id
        self.status = status
        self.tote_type = tote_type
        self.tote_height = tote_height
        self.operator = operator
        self.operator_iph = operator_iph

    id: str
    status: TPStateEnum
    tote_type: Optional[ToteTypeEnum]
    tote_height: Optional[int]
    # TODO what data should i hold here
    operator: str
    # TODO on what timeframe
    operator_iph: int
