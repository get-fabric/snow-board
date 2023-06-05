from typing import Any

from pydantic import BaseModel
from api.model import InfoPerToteType


class InboundResponse(BaseModel):
    invoices: int
    toteTypesNumber: int
    overallLines: int
    itemsToDecant: [InfoPerToteType]

    def __init__(self, invoices: int, toteTypesNumber: int, overallLines: int,
                 itemsToDecant: [InfoPerToteType]) -> None:
        # super().__init__(**data)
        super().__init__()
        self.invoices = invoices
        self.overallLines = overallLines
        self.toteTypesNumber = toteTypesNumber
        self.itemsToDecant = itemsToDecant
