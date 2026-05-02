from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.image_service import InvalidImageError, load_image

router = APIRouter(tags=["frame"])


@router.post("/frame")
async def receive_frame(file: UploadFile = File(...)):
    try:
        await load_image(file)
    except InvalidImageError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {"message": "frame received"}
