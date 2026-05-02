from io import BytesIO

from fastapi import UploadFile
from PIL import Image, UnidentifiedImageError


class InvalidImageError(Exception):
    """Uploaded content could not be decoded as an image."""


async def load_image(file: UploadFile) -> Image.Image:
    data = await file.read()
    if not data:
        raise InvalidImageError("Empty file")

    buffer = BytesIO(data)
    try:
        img = Image.open(buffer)
        img.load()
    except UnidentifiedImageError as exc:
        raise InvalidImageError("File is not a recognized image") from exc
    except Exception as exc:
        raise InvalidImageError("Invalid or corrupted image") from exc

    return img
