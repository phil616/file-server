from pydantic import BaseModel


class FileStorageResp(BaseModel):
    file_id: int
    file_uid: str
    file_name: str
    file_shared: bool
