import uuid
from passlib.handlers.pbkdf2 import pbkdf2_sha256
import hashlib
from datetime import datetime
from core.filelog import Logger

def random_str(type=1):
    if type == 2:
        only = hashlib.md5(str(uuid.uuid4()).encode(encoding='UTF-8')).hexdigest()
        return str(only)
    else:
        only = hashlib.md5(str(uuid.uuid1()).encode(encoding='UTF-8')).hexdigest()
        return str(only)


def gen_file_hash(file: bytes):
    hash_obj = hashlib.sha256()
    hash_obj.update(file)
    return hash_obj.hexdigest()

def show_process_time():
    now = datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    return time_string