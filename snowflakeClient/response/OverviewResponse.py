from pydantic import BaseModel


class OverviewResponse(BaseModel):
    # overview
    # maybe should be listed as avg per hour
    npr: int
    iph: int
    dph: int
    # drill down
    itemsPicked: int
    itemsToPickTotal: int
    itemsDecanted: int
    itemsToDecantTotal: int
    itemsQc: int
    itemsToQcTotal: int
