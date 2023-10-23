from fastapi import FastAPI
from .internal import admin
from .routers import oauth

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
    return {"message": "Hello Bigger Applications!"}
