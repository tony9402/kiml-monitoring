from fastapi import APIRouter
from fastapi import status

from models.status import StatusResponse

router = APIRouter(prefix="")


@router.get(
    "/status",
    responses={
        status.HTTP_200_OK: {"description": "정상"},
    },
    status_code=status.HTTP_200_OK
)
def check_status():
    pass
