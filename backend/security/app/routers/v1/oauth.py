from fastapi import APIRouter

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from typing import Annotated

from ...domains.token import Token
from ...services.access_token import create_oauth_token

router = APIRouter(
    prefix="/oauth",
    tags=["oauth"],
    responses={404: {"description": "Not found"}},
)

@router.post("/token", response_model=Token)
async def oauth_access_token(
    input_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    return create_oauth_token(input_data)
