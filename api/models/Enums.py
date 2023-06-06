from enum import Enum


class ToteTypeEnum(Enum):
    ONE_BIN = "1_bin"
    FOUR_BIN = "4_bins"
    EIGHT_BIN = "8_bins"


class FreeByActionEnum(Enum):
    MERGE = "merge"
    EXPIRED = "expired"


class TPStateEnum(Enum):
    DECANT = "decant"
    MERGE = "merge"
    QC = "qc"
    PICKING_OUT = "picking_out"
    OFF = "off"
