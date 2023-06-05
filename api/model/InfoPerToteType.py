from pydantic import BaseModel
from api.model import ToteTypeEnum


class InfoPerToteType(BaseModel):
    def __init__(self, tote_type: ToteTypeEnum, item_to_decant: int, bins_needed: int, empty_bins_available: int):
        super().__init__()
        self.tote_type = tote_type
        self.item_to_decant = item_to_decant
        self.bins_needed = bins_needed
        self.empty_bins_available = empty_bins_available

    tote_type: ToteTypeEnum
    item_to_decant: int
    bins_needed: int
    empty_bins_available: int
