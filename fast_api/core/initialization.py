from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from start.api import start_router
from start.test_documentation import test_router
from start.work_with_files import file_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="public", html=True))

app.include_router(start_router, tags=["start"])
app.include_router(test_router, tags=["test"])
app.include_router(file_router, tags=["file"])
