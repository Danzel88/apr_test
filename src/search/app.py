from fastapi import FastAPI
from .api import router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static")
