import os


def write_to_path(file: bytes, path: str):
    with open(path, "wb+") as f:
        f.write(file)


def read_from_path(filepath: str):
    with open(filepath, "rb") as f:
        return f.read()
