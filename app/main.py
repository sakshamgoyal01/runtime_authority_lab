from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from auth import authenticate, create_access_token
from config import settings
import os
import socket

app = FastAPI(
    title="Runtime Authority Lab"
)

class LoginRequest(BaseModel):
    username: str
    password: str

@app.get("/")
def root():
    return {
        "message": "Runtime Authority Lab"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/login")
def login(data: LoginRequest):

    valid = authenticate(
        data.username,
        data.password
    )

    if not valid:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": data.username}
    )

    return {
        "access_token": token
    }

@app.get("/runtime-info")
def runtime_info():

    return {
        "hostname": socket.gethostname(),
        "environment": settings.ENVIRONMENT,

        # intentionally exposing env names
        "env_vars": list(os.environ.keys())[:15]
    }

@app.get("/admin")
def admin(x_api_key: str = Header(None)):

    if x_api_key != settings.ADMIN_API_KEY:
        raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

    return {
        "message": "Admin access granted",
        "secret_loaded": bool(
            settings.JWT_SECRET
        )
    }