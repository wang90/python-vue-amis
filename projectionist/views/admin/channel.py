import re
from starlette.requests import Request
from fastapi import APIRouter, BackgroundTasks, HTTPException
from projectionist.amis.base import PAGE as amis_base
from projectionist.libs.template import templates
from projectionist.models.channel import (
    Channel
)
router = APIRouter()


@router.get("/list")
def admin_channel_list(request: Request):
    from projectionist.amis.channel.list import PAGE
    amis_page = {}
    amis_page.update(amis_base)
    amis_page.update(PAGE)
    return templates.TemplateResponse("channel/list.html", {"request": request, "amis_page": amis_page})
