from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from slowapi.errors import RateLimitExceeded

from app.auth import verify_token
from app.services.geocode import geocode_address
from app.rate_limit import limiter, rate_limit_handler

app = FastAPI(title="Maps + AI API")

# Bearer Auth
security = HTTPBearer()

# Rate limit setup
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, rate_limit_handler)


# ROOT ENDPOINT
@app.get("/")
def root():
    return {
        "message": "Welcome to Maps + AI API",
        "endpoints": {
            "geocode": "/geocode?address=YOUR_ADDRESS"
        }
    }


# GEOCODE ENDPOINT 
@app.get("/geocode")
@limiter.limit("5/minute")
def geocode(
    request: Request,
    address: str,
    creds: HTTPAuthorizationCredentials = Depends(security)
):
    # AUTH VALIDATION
    if not creds or not creds.credentials:
        raise HTTPException(status_code=401, detail="Missing token")

    verify_token(creds.credentials)

    # INPUT VALIDATION
    if not address or address.strip() == "":
        raise HTTPException(status_code=400, detail="Address is required")

    try:
        result = geocode_address(address)

        # HANDLE EMPTY RESULT
        if not result:
            raise HTTPException(status_code=404, detail="Address not found")

        return {
            "query": address,
            "result": result
        }

    except Exception as e:
        # ERROR HANDLING 
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error: {str(e)}"
        )