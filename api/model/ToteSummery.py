from api.model import ToteTypeEnum


class ToteSummery:

    def __init__(self,height: int, tote_type_enum: ToteTypeEnum, amount: int, empty: int, occupied: int, empty_potential: int, unclean: int):
        super().__init__()
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
