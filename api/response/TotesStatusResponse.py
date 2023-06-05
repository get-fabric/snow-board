from pydantic import BaseModel
from api.model import ToteSummery


class TotesStatusResponse(BaseModel):
    TotesSummery: [ToteSummery]
