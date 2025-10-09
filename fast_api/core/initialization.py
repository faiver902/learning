from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from start.api import start_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="public", html=True))

app.include_router(start_router)
