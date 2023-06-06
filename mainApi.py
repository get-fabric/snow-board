from typing import Annotated, Union
from fastapi import FastAPI, Path, Query
from starlette import status
from api.models.Responses import *

# from fastapi_route_logger_middleware import RouteLoggerMiddleware
# from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


# app.include_router(auth.router)


# Instrumentator().instrument(app).expose(app)
# app.add_middleware(RouteLoggerMiddleware)
# def checkForExceptions(mfc: str):
#     raise HTTPException(status_code=404, detail="mfc not foud")
#     raise HTTPException(status_code=401, detail="auth required")


@app.get("/overview/{mfc_id}", status_code=status.HTTP_200_OK)
async def get_overview(
        mfc_id: str = Path(min_length=5, max_length=10, regex="MFC_+\\d"),
        time_frame: Annotated[Union[int, None], Query(title="default is 3", gt=0)] = 3):
    ##TODO checkForExceptions()
    # ipty: InfoPerToteType = InfoPerToteType(ToteTypeEnum.ONE_BIN, 0, 0, 0)
    return OverviewResponse(0, 0, 0, 0, 0, 0, 0, 0, 0)
    # return {"mfc_id": mfc_id, "time_frame": time_frame}


@app.get("/inbound/{mfc_id}", status_code=status.HTTP_200_OK)
async def get_inbound(
        mfc_id: str = Path(min_length=5, max_length=10, regex="MFC_+\\d"),
        time_frame: Annotated[Union[int, None], Query(title="default is 3", gt=0)] = 3):
    ##TODO checkForExceptions()
    ipti = InfoPerToteType(ToteTypeEnum.ONE_BIN, 0, 0, 0)
    ipti1 = InfoPerToteType(ToteTypeEnum.FOUR_BIN, 0, 0, 0)
    iptis = [ipti, ipti1]

    return InboundResponse(0, 0, 0, iptis)


@app.get("/operational_tasks/{mfc_id}", status_code=status.HTTP_200_OK)
async def get_operational_tasks(
        mfc_id: str = Path(min_length=5, max_length=10, regex="MFC_+\\d"),
        time_frame: Annotated[Union[int, None], Query(title="default is 3", gt=0)] = 3):
    ##TODO checkForExceptions()
    qc = QC(0, 0, 0, 0, 0, 0, 0)
    tx = ToteExtraction(0, 0, 0, 0)
    dict_sub = {FreeByActionEnum.MERGE: 0, FreeByActionEnum.EXPIRED: 0}
    dict_p = {ToteTypeEnum.ONE_BIN: dict_sub, ToteTypeEnum.FOUR_BIN: dict_sub}
    to = ToteOptimization(dict_p)
    return OperationalTasksResponse(qc, tx, to)


@app.get("/tote_status/{mfc_id}", status_code=status.HTTP_200_OK)
async def get_tote_status(
        mfc_id: str = Path(min_length=5, max_length=10, regex="MFC_+\\d"),
        time_frame: Annotated[Union[int, None], Query(title="default is 3", gt=0)] = 3):
    ##TODO checkForExceptions()
    ts = ToteSummery(250, ToteTypeEnum.ONE_BIN, 0, 0, 0, 0, 0)
    ts1 = ToteSummery(360, ToteTypeEnum.FOUR_BIN, 0, 0, 0, 0, 0)
    tss = [ts, ts1]
    return TotesStatusResponse(tss)


@app.get("/site_resources/{mfc_id}", status_code=status.HTTP_200_OK)
async def get_site_resources(
        mfc_id: str = Path(min_length=5, max_length=10, regex="MFC_+\\d"),
        time_frame: Annotated[Union[int, None], Query(title="default is 3", gt=0)] = 3):
    ##TODO checkForExceptions()
    tpi1 = TPInfo("", TPStateEnum.MERGE, None, 0, "no-one", 0)
    tpi2 = TPInfo("", TPStateEnum.QC, None, 0, "no-two", 0)
    tps = [tpi1, tpi2]
    return SiteResourcesResponse(tps)
