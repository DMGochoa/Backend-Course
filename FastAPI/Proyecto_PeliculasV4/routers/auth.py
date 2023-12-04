from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User

auth_router = APIRouter()


@auth_router.post("/login", tags=['auth'], response_model=dict, status_code=200)
def login(user: User) -> dict:
    if user.email == "admin@gmail.com" and user.password == "admin":
        token = create_token(data=user.model_dump())
        return JSONResponse(content={"token": token}, 
                            status_code=200)
    else:
        return JSONResponse(content={"message": "Invalid credentials"},
                            status_code=401)