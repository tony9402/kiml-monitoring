import json
import datetime

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select

from models.status import StatusDao
from postgresdb import get_db_session
from redisdb import get_redis_sess

router = APIRouter(prefix="/dashboard")

templates = Jinja2Templates(directory="templates")


@router.get("/kiml", response_class=HTMLResponse)
async def dashboard(request: Request, db=Depends(get_db_session)):
    query = select(StatusDao).order_by(StatusDao.create_time.desc())
    result = await db.execute(query)
    datas = result.fetchall()
    logs = [x[0].__dict__ for x in datas]
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request, 
            "logs": logs, 
            "timezone": datetime.timezone(datetime.timedelta(hours=9))
        }
    )  # noqa: E501


@router.get(path="/submit", response_class=HTMLResponse)
async def show_submit(request: Request, db=Depends(get_redis_sess)):
    logs = []
    for key, value in db.hgetall("status").items():
        query = db.hget("run_info", key)
        query = json.loads(query)
        logs.append(
            {
                "uuid": key,
                "status": value,
                "run_name": query["run_name"],
            }
        )
    return templates.TemplateResponse(
        "status.html",
        {
            "request": request,
            "logs": logs,
            "timezone": datetime.timezone(datetime.timedelta(hours=9)),
        },
    )
