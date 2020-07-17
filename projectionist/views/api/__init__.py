from starlette.requests import Request
from fastapi import (
    APIRouter,
    Form,
    File,
    BackgroundTasks,
    UploadFile,
)


router = APIRouter()
# router.include_router(book.router, prefix="/book")
# router.include_router(user.router, prefix="/user")
# router.include_router(dialogue.router, prefix="/dialogue")
# router.include_router(actor.router, prefix="/actor")




@router.post("/upload")
async def api_upload(
    request: Request,
    file: UploadFile = File(...)):
    
    content = await file.read()
    uf = await FileImage.upload(name=file.filename, content=content)
    if not uf:
        result = {
            "status": -1,
        }
        return result
    result = {
        "status": 0,
        "data": {
            "value": uf.url,
            "url": uf.url,
            "filename": uf.name,
        }
    }
    return result

@router.post("/upload/file")
async def api_upload_file(
    request: Request,
    file: UploadFile = File(...)):

    print(file)
    content = await file.read()
    name = file.filename
    content = str(content,"utf-8")
    # data = content.splitlines()
    data = content

    if len(data) <= 0 :
        return {"stauts":-1,"msg":"没有内容"}
    write_status = False

    uf = await FileTxt.upload(name = name, content = content)
    
    server_id = ""
    if uf :
        serverFile = uf.to_json()
        print(serverFile)
        server_id = serverFile['_id']
        write_status = True
    if not uf or write_status == False:
        return { "status": -1, "msg": "上传失败" }

    return {
        "status": 0,
        "msg": "上传成功",
        "data": {
            # "value": server_id,
            "url": uf.url,
            "filename": uf.name,
            "content": data,
            "server_id": server_id,
        }
    }

