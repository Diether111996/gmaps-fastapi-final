import os
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

def verify_token(token: str):
    if not token or token != API_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing token"
        )