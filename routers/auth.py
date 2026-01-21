from fastapi import APIRouter
from pydantic import BaseModel
from core_functions.auth_functions import signup_user, login_user

router = APIRouter(prefix="/auth", tags=["Auth"])

# ---------- Request Models ----------
class SignupRequest(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

# ---------- SIGNUP ----------
@router.post("/signup")
async def signup(data: SignupRequest):
    return await signup_user(data.username, data.password)

# ---------- LOGIN ----------
@router.post("/login")
async def login(data: LoginRequest):
    return await login_user(data.username, data.password)
