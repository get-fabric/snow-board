from typing import Dict, List
from typing import Optional
from api.models.Enums import ToteTypeEnum, FreeByActionEnum, TPStateEnum


class InfoPerToteType:
    def __init__(self, tote_type: ToteTypeEnum, item_to_decant: int, bins_needed: int,
                 empty_bins_available: int):
        self.tote_type = tote_type
        self.item_to_decant = item_to_decant
        self.bins_needed = bins_needed
        self.empty_bins_available = empty_bins_available

    tote_type: ToteTypeEnum
    item_to_decant: int
    bins_needed: int
    empty_bins_available: int


class QC:
    def __init__(self, total_items: int, total_bins: int, stock_take: int, totes: int, sku: int,
                 invoice_lines: int,
                 limbo: int):
        self.total_items = total_items
        self.total_bins = total_bins
        self.stock_take = stock_take
        self.totes = totes
        self.sku = sku
        self.invoice_lines = invoice_lines
        self.limbo = limbo

    total_items: int
    total_bins: int
    # TODO need to understand that shit
    stockTake: int
    totes: int
    sku: int
    invoiceLines: int
    # TODO limbo what? items? lines?
    limbo: int


class ToteExtraction:
    def __init__(self, clean: int, new_sticker: int, damaged: int, prepping: int):
        self.clean = clean
        self.new_sticker = new_sticker
        self.damaged = damaged
        self.prepping = prepping

    clean: int
    new_sticker: int
    damaged: int
    # TODO what is that?
    prepping: int


class ToteOptimization:
    def __init__(self,
                 free_by_action_and_type: Dict[ToteTypeEnum, Dict[FreeByActionEnum, int]]):
        self.free_by_action_and_type = free_by_action_and_type

    free_by_action_and_type: Dict[ToteTypeEnum, Dict[FreeByActionEnum, int]]


class ToteSummery:
    def __init__(self, height: int, tote_type_enum: ToteTypeEnum, amount: int,
                 empty: int, occupied: int,
                 empty_potential: int, unclean: int):
        self.height = height
        self.tote_type_enum = tote_type_enum
        self.amount = amount
        self.empty = empty
        self.occupied = occupied
        self.empty_potential = empty_potential
        self.unclean = unclean

    height: int
    tote_type_enum: ToteTypeEnum
    amount: int
    empty: int
    occupied: int
    empty_potential: int
    unclean: int


class TPInfo:
    tp_id: str
    status: TPStateEnum
    tote_type: Optional[ToteTypeEnum]
    tote_height: Optional[int]
    operator: str
    # TODO on what timeframe - maya
    operator_iph: int

    def __init__(self, tp_id: str, status: TPStateEnum, tote_type: Optional[ToteTypeEnum],
                 tote_height: Optional[int], operator: str, operator_iph: int):
        self.tp_id = tp_id
        self.status = status
        self.tote_type = tote_type
        self.tote_height = tote_height
        self.operator = operator
        self.operator_iph = operator_iph


class FreeUpBinTips:
    class ToteOptimization:
        toteType: int
        freeByAction: Dict[FreeByActionEnum, int]

    totesCanBeOptimized: List[ToteOptimization]
