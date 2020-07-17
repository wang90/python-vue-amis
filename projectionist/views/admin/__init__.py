from copy import deepcopy
from starlette.requests import Request
from fastapi import APIRouter
from starlette.responses import JSONResponse
from projectionist.amis.base import PAGE as amis_base
from projectionist.libs.template import templates
from projectionist.models.admin import AdminPage

from projectionist.views.admin import channel



router = APIRouter()
router.include_router(channel.router, prefix="/channel")

@router.get("/")
async def admin_index(request: Request):
    from projectionist.amis.index import PAGE
    amis_page = {}
    amis_page.update(amis_base)
    amis_page.update(PAGE)
    items = await AdminPage.get_list()
    amis_data = {"items": items}
    print('admin')
    return templates.TemplateResponse("base.html",
        {
            "request": request,
            "amis_page": amis_page,
            "amis_data": amis_data,
        })