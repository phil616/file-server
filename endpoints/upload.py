import os
from fastapi import APIRouter, UploadFile
from core.utils import random_str, gen_file_hash
from config import settings
from schemas.response import FileStorageResp
from models.base import FileList
from schemas.file import FileInfo, FileMetaInfo
from core import persistence

upload_route = APIRouter(prefix="/upload",tags=["Upload"])


@upload_route.post("/new", response_model=FileStorageResp)
async def upload_new_file(file: UploadFile):
    fileBytes = file.file.read()
    fileHash = gen_file_hash(fileBytes)
    fileName = file.filename
    file.file.seek(0, 2)
    fileSize = file.file.tell()
    fileMIME = file.content_type
    fileId = random_str()
    filePath = os.path.join(*settings.SINGLE_FILE_STORAGE_PATH, fileId)
    info = FileMetaInfo(
        **(FileInfo(
            file_id=fileId,
            file_name=fileName,
            file_size=fileSize,
            file_mime_type=fileMIME,
            file_path=filePath
        ).dict())
        ,
        file_hash=fileHash
    )
    persistence.write_to_path(fileBytes, filePath)
    newFile = await FileList.create(**info.dict())
    resp = FileStorageResp(file_id=newFile.pk, file_uid=fileId, file_name=fileName, file_shared=False)
    return resp


@upload_route.post("/default", response_model=FileStorageResp)
async def upload_default_file(file: UploadFile):
    fileBytes = file.file.read()
    fileHash = gen_file_hash(fileBytes)
    db_file = await FileList.filter(file_hash=fileHash).first()
    if db_file is not None:
        fileName = file.filename
        info = FileMetaInfo(
            file_name=fileName,  # unique
            file_id=db_file.file_id,
            file_size=db_file.file_size,
            file_mime_type=db_file.file_mime_type,
            file_path=db_file.file_path
        )
        newFile = await FileList.create(**info.dict())
        resp = FileStorageResp(file_id=newFile.pk, file_uid=db_file.file_id, file_name=fileName, file_shared=True)
        return resp
    else:
        fileBytes = file.file.read()
        fileHash = gen_file_hash(fileBytes)
        fileName = file.filename
        file.file.seek(0, 2)
        fileSize = file.file.tell()
        fileMIME = file.content_type
        fileId = random_str()
        filePath = os.path.join(*settings.SINGLE_FILE_STORAGE_PATH, fileId)
        info = FileMetaInfo(
            **(FileInfo(
                file_id=fileId,
                file_name=fileName,
                file_size=fileSize,
                file_mime_type=fileMIME,
                file_path=filePath
            ).dict())
            ,
            file_hash=fileHash
        )
        persistence.write_to_path(fileBytes, filePath)
        newFile = await FileList.create(**info.dict())
        resp = FileStorageResp(file_id=newFile.pk, file_uid=fileId, file_name=fileName, file_shared=False)
        return resp
