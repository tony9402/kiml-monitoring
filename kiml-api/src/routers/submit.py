import json
import time
from uuid import uuid4

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from models.job import CancelDto, SubmitDto
from redisdb import get_redis_sess

router = APIRouter(prefix="")


@router.post("/submit", response_class=JSONResponse)
async def submit(
    request: Request,
    response: JSONResponse,
    data: SubmitDto,
    db=Depends(get_redis_sess),
):
    current_time = time.time()
    save_data: dict = data.dict()
    save_data["uuid"] = uuid4().__str__()
    query = json.dumps(save_data, ensure_ascii=False)
    db.zadd("submit_jobs", {query: current_time})
    db.hset("run_info", save_data["uuid"], value=query)
    db.hset("status", save_data["uuid"], value="Pending...")
    return {}


@router.delete(path="/cancel", response_class=JSONResponse)
async def cancel(data: CancelDto, db=Depends(get_redis_sess)):
    query_info = db.hget("run_info", data.uuid)
    result = db.zrem("submit_jobs", query_info)
    if result == 1:
        db.hset("status", data.uuid, "Canceled")
    return JSONResponse({"result": result})
