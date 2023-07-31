from fastapi import APIRouter
from fastapi import status

from models.login import LoginRequest, LoginResponse

router = APIRouter(prefix="")


@router.post(
    "/login",
    responses={
        status.HTTP_200_OK: {"description": "로그인 성공"},
        status.HTTP_401_UNAUTHORIZED: {"description": "로그인 실패"},
    },
    response_model=LoginResponse,
    status_code=status.HTTP_200_OK,
)
def kiml_login(
    request: LoginRequest,
):
    return LoginResponse()