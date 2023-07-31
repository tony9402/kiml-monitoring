from fastapi import APIRouter

router = APIRouter(prefix="/experiments")


@router.get("/")
def show_all_experiments():
    return None
