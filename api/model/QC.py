from pydantic import BaseModel


class QC(BaseModel):
    def __init__(self, total_items: int, total_bins: int, stock_take: int, totes: int, sku: int, invoice_lines: int,
                 limbo: int):
        super().__init__()
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
