

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from models.base import FileList

download_route = APIRouter(prefix="/download",tags=["Download"])


def abstract_file_gen(file: FileList):
    filePath = file.file_path
    fileName = file.file_name
    fileType = file.file_mime_type
    return FileResponse(filePath, media_type=fileType, filename=fileName)


@download_route.get("/uid")
async def download_by_uid(uid: str):
    file = await FileList.filter(file_id=uid).first()
    if file is None:
        raise HTTPException(404, "file not found")
    return abstract_file_gen(file)


@download_route.get("/rid")
async def download_by_rid(rid: int):
    file = await FileList.filter(pk=rid).first()
    if file is None:
        raise HTTPException(404, "file not found")
    return abstract_file_gen(file)
