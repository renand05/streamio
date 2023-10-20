from fastapi import FastAPI
from .internal import admin
from .routers import oauth

app = FastAPI()

app.include_router(oauth.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
