from fastapi import FastAPI
from app.internal import admin
from app.routers.v1 import oauth

server = FastAPI()

server.include_router(oauth.router)
server.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    responses={418: {"description": "I'm a teapot"}},
)

@server.get("/")
async def root():
    return {"message": "Hello World"}
