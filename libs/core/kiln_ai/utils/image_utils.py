import base64
from pathlib import Path


def image_file_to_base64(path: str | Path) -> str:
    """Read an image from a file and return a base64 encoded string."""
    with open(Path(path), "rb") as img_file:
        data = img_file.read()
    return base64.b64encode(data).decode("utf-8")
