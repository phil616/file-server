from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from fastapi import UploadFile


class FileInfo(BaseModel):
    file_id: str
    file_name: str
    file_size: int
    file_mime_type: str
    file_path: str


class FileMetaInfo(FileInfo):
    file_owner: Optional[str] = None
    file_permission: Optional[str] = None
    file_hash: Optional[str] = None
    file_is_crypt: bool = False
    file_is_compressed: bool = False
    file_info: Optional[str] = None



class SingleFileUpload(BaseModel):
    file: UploadFile


class FileUpload(BaseModel):
    file: UploadFile
    owner: str
    permission: str
    hash: str
    isEncrypt: bool
    info: str
