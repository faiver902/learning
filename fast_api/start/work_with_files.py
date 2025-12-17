import os

import aiofiles
from starlette import status
from starlette.responses import StreamingResponse, FileResponse
from pathlib import Path

from fastapi import UploadFile, File, HTTPException, APIRouter

UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

file_router = APIRouter()


@file_router.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    safe_filename = os.path.basename(file.filename)
    file_path = os.path.join(UPLOAD_DIR, safe_filename)

    try:
        async with aiofiles.open(file_path, 'wb') as out_file:
            while chunk := await file.read(1024 * 1024):
                await out_file.write(chunk)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"There was an error uploading the file: {e}")
    finally:
        await file.close()

    return {"message": f"Successfully uploaded {safe_filename}", "path": file_path}


@file_router.get("/download/")
async def get_file(name: str):
    safe_name = os.path.basename(name)
    file_path = Path(UPLOAD_DIR) / safe_name

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail={"requested": name, "safe_name": safe_name, "abs_path": str(file_path.resolve())},
        )
    return FileResponse(
        path=f"{UPLOAD_DIR}/{name}",
        filename=name,
        # media_type='application/octet-stream'
    )


@file_router.get("/stream-file/")
async  def stream_large_file(name: str):
    def iterfile():
        # Open in binary mode
        with open(f"{UPLOAD_DIR}/{name}", mode="rb") as file_like:
            yield from file_like

    headers = {
        'Content-Disposition': 'attachment; filename="video_stream.mp4"'
    }
    return StreamingResponse(
        iterfile(),
        headers=headers,
        media_type="video/mp4"
    )