from starlette.requests import Request
from starlette.templating import Jinja2Templates
from fastapi import (
    APIRouter,
    Form,
    File,
    BackgroundTasks,
    UploadFile,
)


router = APIRouter()
templates = Jinja2Templates(directory="projectionist/dist")

@router.get("/")
async def web_home(
        request: Request,
        ostype: str = ''
    ):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)