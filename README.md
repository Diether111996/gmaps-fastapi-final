# FastAPI Maps Integration API

## Project Description

This project is a FastAPI-based backend application that integrates geocoding services to convert addresses into geographic coordinates. It includes secure authentication and rate limiting to simulate a production-ready API.

---

## Features

* Geocoding endpoint (convert address → latitude/longitude)
* Bearer Token Authentication
* Rate Limiting (anti-abuse protection)
* Modular and scalable architecture

---

## Prerequisites

* Python 3.10+
* Internet connection

---

## Installation

```bash
git clone <your-repo-url>
cd your-project
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the root directory:

```env
API_TOKEN=your_token_here
```

---

## Project Structure

```
app/
 ├── main.py
 ├── auth.py
 ├── rate_limit.py
 ├── services/
 │    ├── geocode.py
.env
requirements.txt
README.md
.gitignore
```

---

## API Endpoints

### GET /geocode

Returns latitude and longitude of a given address.

**Query Parameter:**

* `address` (string)

**Example Response:**

```json
{
  "query": "Quezon City",
  "result": {
    "lat": 14.6760,
    "lng": 121.0437
  }
}
```

---

## Authentication

All endpoints require Bearer Token:

```
Authorization: Bearer your_token_here
```

---

## 🚦 Rate Limiting

* `/geocode` → 5 requests per minute

If exceeded:

```
429 Too Many Requests
```

---

## Testing Instructions

### 1. Start the Server

```
uvicorn app.main:app --reload
```

---

### 2. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

### 3. Authorize

Click **Authorize** and enter:

```
Bearer your_token_here
```

---

### 4. Test Geocode Endpoint

* Enter address (e.g., *Quezon City*)
* Click Execute

---

### 5. cURL Testing

```bash
curl -X GET "http://127.0.0.1:8000/geocode?address=Quezon City" \
-H "Authorization: Bearer your_token_here"
```

---

### 6. Test Rate Limiting

Send more than 5 requests quickly.

Expected result:

```
429 Too Many Requests
```

---

### 7. Test Authentication Failure

Use:

* Wrong token
* No token

Expected result:

```
401 Unauthorized
```

---

## Troubleshooting Guide

### Server Won’t Start

* Run: `pip install -r requirements.txt`
* Install uvicorn: `pip install uvicorn`

---

### Port Already in Use

```
uvicorn app.main:app --reload --port 8001
```

---

### 401 Unauthorized

Check header format:

```
Authorization: Bearer your_token_here
```

---

### 429 Too Many Requests

Wait 1 minute before retrying.

---

### Geocoding Returns Empty Result

* Use a complete address (e.g., *Quezon City, Philippines*)
* Check internet connection

---

### .env Not Working

Make sure:

```
from dotenv import load_dotenv
load_dotenv()
```

---

###  CORS Issues (Optional)

```
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Team Members

* Member 1 – Backend / Authentication
* Member 2 – API Integration
* Member 3 – Testing / Documentation
* Member 4 – Presentation


