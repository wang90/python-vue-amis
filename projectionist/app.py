import os
from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from projectionist.views.admin import router as admin_router
from projectionist.views.web import router as web_router
from projectionist.views.api import router as api_router
from projectionist.views.v1 import router as v1_router

from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount
from starlette.applications import Starlette
from starlette.config import Config

# from projectionist.libs.sentry import SentryMiddleware
from projectionist.config import (
    PROJECT_NAME,
)

app = FastAPI(title=PROJECT_NAME, openapi_url="/api/v1/openapi.json")

origins = [
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8088",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(SentryMiddleware)


# 配置前端静态文件目录
app.mount("/js", StaticFiles(directory="projectionist/dist/js"), name="js")
app.mount("/css", StaticFiles(directory="projectionist/dist/css"), name="css")
app.mount("/img", StaticFiles(directory="projectionist/dist/img"), name="img")
app.mount("/static", StaticFiles(directory="projectionist/static"), name="static")

app.include_router(admin_router,prefix="/admin")
app.include_router(api_router,prefix="/api")
app.include_router(v1_router,prefix="/v1")
app.include_router(web_router,prefix="/web")








