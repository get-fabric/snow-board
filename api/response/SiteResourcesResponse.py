from pydantic import BaseModel
class SiteResourcesResponse(BaseModel):
    tps:[TPInfo]