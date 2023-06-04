from pydantic import BaseModel
class QC(BaseModel):
    totalItems: int
    totalBins: int
    # TODO need to understand that shit
    stockTake: int
    totes: int
    sku: int
    invoiceLines: int
    # TODO limbo what? items? lines?
    limbo: int