import os
import json
import time
from uuid import uuid4

from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse, Response

from models.job import CancelDto, SubmitDto
from redisdb import get_redis_sess

router = APIRouter(prefix="")


def cal_gpus(instance: str) -> float:
    return float(instance.split("A")[0])


@router.post("/submit", response_class=JSONResponse)
async def submit(
    request: Request,
    response: Response,
    data: SubmitDto,
    db=Depends(get_redis_sess),
):
    max_gpus = float(os.environ["KIML_GPU_QUOTA"])
    if cal_gpus(data.instance_type) > max_gpus:
        return JSONResponse(
            content="Quota exceed", status_code=status.HTTP_406_NOT_ACCEPTABLE
        )
    current_time = time.time()
    save_data: dict = data.dict()
    save_data["uuid"] = uuid4().__str__()
    query = json.dumps(save_data, ensure_ascii=False)
    db.zadd("submit_jobs", {query: current_time})
    db.hset("run_info", save_data["uuid"], value=query)
    db.hset("status", save_data["uuid"], value="Pending...")
    return JSONResponse(content="Submit !", status_code=status.HTTP_200_OK)


@router.delete(path="/cancel", response_class=JSONResponse)
async def cancel(data: CancelDto, db=Depends(get_redis_sess)):
    query_info = db.hget("run_info", data.uuid)
    result = db.zrem("submit_jobs", query_info)
    if result == 1:
        db.hset("status", data.uuid, "Canceled")
        return JSONResponse(
            content="Canceled !", status_code=status.HTTP_200_OK
        )  # noqa: E501
    return JSONResponse(
        content="Already Done", status_code=status.HTTP_404_NOT_FOUND
    )  # noqa: E501
