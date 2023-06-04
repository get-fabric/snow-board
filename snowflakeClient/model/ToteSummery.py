from snowflakeClient.model import ToteTypeEnum


class ToteSummery():
    height: int
    toteTypeEnum: ToteTypeEnum
    amount: int
    empty: int
    occupied: int
    emptyPotential: int
    unclean: int
