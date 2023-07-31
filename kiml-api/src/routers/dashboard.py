from fastapi import APIRouter
from fastapi import status, Depends
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="")

templates = Jinja2Templates(directory="templates")

@router.get(
    "/dashboard",
    response_class=HTMLResponse,
)
async def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "logs": []})
