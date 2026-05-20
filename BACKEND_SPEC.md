# Backend API Specification — `api.sensorcensor.xyz/festivalin`

This document defines the FastAPI backend that receives printed sticker images from the **Stikka Factory** (printit) Streamlit app.

## 1. Overview

The Stikka Factory is a Streamlit-based web app that connects to a Brother QL label printer. Users upload images, take webcam photos, generate images from text prompts, etc. — and print them on thermal labels.

**New behaviour:** Every time an image is successfully printed, the app sends a copy of that image (the raw PNG) to `https://api.sensorcensor.xyz/festivalin` via an HTTP `POST` with a multipart/form-data file upload.

You are building the FastAPI server that receives these images.

---

## 2. How the Client Sends the Image

From `printer_utils.py` in the printit project:

```python
def send_image_to_webhook(image_path):
    with open(image_path, "rb") as img_file:
        files = {"image": ("sticker.png", img_file, "image/png")}
        response = requests.post(WEBHOOK_URL, files=files, timeout=30)
```

**What this means for the backend:**

| Aspect | Value |
|---|---|
| HTTP Method | `POST` |
| URL path | `/festivalin` |
| Content-Type | `multipart/form-data` |
| Field name | `image` |
| Filename sent | `sticker.png` |
| MIME type | `image/png` |
| Timeout (client side) | 30 seconds (server should respond well before that) |
| Auth / Headers | **None currently** (the client does not send any auth headers; you may add an API key later) |

### Client-side error handling (for awareness)

The client logs failures but **never** retries or blocks the print. The webhook is purely a "fire and forget" side-effect. This means:
- The server should be reliable, but if it's down the print still works.
- You may want to add a simple shared secret / API key in the future (configurable from `config.toml`).

---

## 3. API Endpoints

### 3.1 `POST /festivalin`

Receive a PNG image that was just printed.

**Request:**

```
POST /festivalin
Content-Type: multipart/form-data

image: <binary PNG data>
```

**Success Response:**

```json
{
  "status": "ok",
  "message": "Image received",
  "filename": "sticker.png",
  "size_bytes": 123456
}
```

Status code: `200 OK`

**Error Responses:**

| Status | Body | When |
|---|---|---|
| `400 Bad Request` | `{"status": "error", "message": "No image file provided"}` | Missing `image` field |
| `400 Bad Request` | `{"status": "error", "message": "Uploaded file is not a valid PNG image"}` | File exists but isn't valid PNG |
| `413 Payload Too Large` | `{"status": "error", "message": "File too large. Maximum size is 10 MB"}` | Image exceeds size limit |
| `500 Internal Server Error` | `{"status": "error", "message": "..."}` | Storage or processing failure |

**Size limits:**

- Max file size: **10 MB** (client images are typically small dithered black-and-white PNGs, often under 500 KB)

### 3.2 `GET /health`

Simple health-check endpoint.

**Request:**

```
GET /health
```

**Response:**

```json
{
  "status": "ok",
  "service": "festivalin-receiver",
  "version": "0.1.0"
}
```

Status code: `200 OK`

---

## 4. Image Characteristics (What You'll Receive)

These are Brother QL thermal printer outputs. Key facts:

| Property | Typical Value |
|---|---|
| Format | PNG (always) |
| Colour mode | **1-bit black & white** (dithered) — `PIL mode '1'` |
| Dimensions | Width is fixed to the label width in dots; height varies |
| Label widths | 12, 29, 38, 50, 54, 62, 102, 103, 104 mm (dots vary by model) |
| File size | Usually **50–300 KB** |
| Content | Anything — uploaded photos, AI-generated images, text labels with QR codes, etc. |

**Important:** The image is already the **final printed version** (dithered, resized, thresholded). Nothing needs to be processed on the server side — just store it.

---

## 5. Storage Requirements

The server should **persist received images**. Choose whatever makes sense:

### Minimum viable storage
- **Local filesystem** with a timestamped directory structure:
  ```
  /data/uploads/
    ├── 2026/
    │   ├── 05/
    │   │   ├── 21/
    │   │   │   ├── 1716240000_sticker.png
    │   │   │   └── 1716240123_sticker.png
    │   │   └── 22/
    │   └── 06/
    └── ...
  ```
  The filename prefix should be a Unix timestamp so ordering is implicit.

### Better storage (recommended for production)
- **Object storage** (S3 / MinIO / R2) with a key pattern like:
  ```
  festivalin/2026/05/21/<uuid>_<unix_timestamp>.png
  ```
- **SQLite or PostgreSQL** metadata table:
  ```sql
  CREATE TABLE printed_images (
      id            UUID PRIMARY KEY,
      filename      TEXT NOT NULL,
      original_name TEXT,
      file_size     INTEGER NOT NULL,
      storage_path  TEXT NOT NULL,
      storage_type  TEXT NOT NULL DEFAULT 'local',
      content_type  TEXT NOT NULL DEFAULT 'image/png',
      image_width   INTEGER,
      image_height  INTEGER,
      created_at    TIMESTAMP NOT NULL DEFAULT NOW()
  );
  ```

---

## 6. Future / Nice-to-Have Features (Not Required Now)

These are things the project might want later. Design your storage and API flexibly.

- **Authentication** — Add an `X-API-Key` header check (configurable via environment variable)
- **GET /images** — List recently received images (paginated, with thumbnails)
- **GET /images/{id}** — Download a specific received image
- **DELETE /images/{id}** — Admin endpoint to delete stored images
- **Web dashboard** — Simple HTML page showing the gallery of received stickers
- **Rate limiting** — Per-IP or global rate limit
- **Webhook forwarding** — Forward received images to another endpoint (e.g., Telegram, Discord, Slack)
- **Image metadata extraction** — QR code detection, OCR on the label content

---

## 7. Deployment Notes

- The server should run behind a reverse proxy (nginx / Caddy) with TLS (Let's Encrypt).
- The domain `api.sensorcensor.xyz` already exists; you just need to set up the `/festivalin` route.

### Recommended stack

| Component | Suggestion |
|---|---|
| Framework | **FastAPI** (as specified) |
| ASGI Server | **Uvicorn** |
| File storage | Local FS for dev, **MinIO / S3** for prod |
| Metadata DB | **SQLite** (simple) or **PostgreSQL** (if you want to scale) |
| Deployment | **Docker** with `docker-compose` |
| Validation | **Pydantic** (built into FastAPI) |

### Environment variables

```bash
# Required
STORAGE_PATH=/data/uploads           # Local storage directory
MAX_FILE_SIZE=10485760               # 10 MB

# Optional
API_KEY=                             # If/when auth is added
DATABASE_URL=sqlite:///data/db.sqlite # Metadata database
S3_ENDPOINT=                         # S3-compatible storage
S3_BUCKET=festivalin-uploads
S3_ACCESS_KEY=
S3_SECRET_KEY=
```

---

## 8. Example FastAPI Starter

Here's a minimal starting point to illustrate the expected interface:

```python
# main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
import uuid
import os
from datetime import datetime

app = FastAPI(title="Festivalin Image Receiver")
MAX_SIZE = 10 * 1024 * 1024  # 10 MB

@app.post("/festivalin")
async def receive_image(image: UploadFile = File(...)):
    if not image:
        raise HTTPException(400, detail="No image file provided")

    contents = await image.read()
    if len(contents) > MAX_SIZE:
        raise HTTPException(413, detail="File too large. Maximum size is 10 MB")

    if not contents.startswith(b"\x89PNG"):
        raise HTTPException(400, detail="Uploaded file is not a valid PNG image")

    now = datetime.utcnow()
    dir_path = f"/data/uploads/{now.year}/{now.month:02d}/{now.day:02d}"
    os.makedirs(dir_path, exist_ok=True)

    file_id = uuid.uuid4().hex
    ts = int(now.timestamp())
    file_path = f"{dir_path}/{ts}_{file_id}.png"

    with open(file_path, "wb") as f:
        f.write(contents)

    return {
        "status": "ok",
        "message": "Image received",
        "filename": image.filename or "sticker.png",
        "size_bytes": len(contents),
    }

@app.get("/health")
async def health():
    return {"status": "ok", "service": "festivalin-receiver", "version": "0.1.0"}
```

---

## 9. Testing

You can test the endpoint with curl:

```bash
# Send a real PNG file
curl -X POST https://api.sensorcensor.xyz/festivalin \
  -F "image=@test_sticker.png"

# Send a non-PNG file (should get 400)
echo "not a png" > fake.png
curl -X POST https://api.sensorcensor.xyz/festivalin \
  -F "image=@fake.png"

# Health check
curl https://api.sensorcensor.xyz/festivalin/../health
```

---

## 10. Contact / Context

This project is the "Stikka Factory" — a sticker printing station for events (originally built at CCC Camp 2023). The webhook feature was added so every sticker printed gets archived on the server. The URL `/festivalin` is named after the event context.

For questions about the client-side code, see:
- `/home/jonathan/Desktop/printit/printer_utils.py` — the `send_image_to_webhook()` function
- `/home/jonathan/Desktop/printit/config.toml` — the `webhook_*` settings
