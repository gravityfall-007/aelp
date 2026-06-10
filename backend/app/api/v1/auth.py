from fastapi import APIRouter, HTTPException
import jwt
from datetime import datetime, timedelta

router = APIRouter()

SECRET = "supersecret"

@router.post("/login")
def login(username: str, password: str):
    if username != "admin" or password != "admin":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=6)
    }

    token = jwt.encode(payload, SECRET, algorithm="HS256")

    return {"access_token": token}