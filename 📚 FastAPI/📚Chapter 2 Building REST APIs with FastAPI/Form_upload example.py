from fastapi import FastAPI, Form, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import os

app = FastAPI(title="Real-Life Form and File Upload Example")

# Create directories for templates and uploads if they don't exist
os.makedirs("templates", exist_ok=True)
os.makedirs("uploads", exist_ok=True)

# Mount templates folder (for rendering HTML)
templates = Jinja2Templates(directory="templates")

# Serve uploaded files (optional)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Route: Show HTML form
@app.get("/", response_class=HTMLResponse)
def show_form(request: Request):
    """
    Display the upload form when visiting the root URL.
    """
    return templates.TemplateResponse("form.html", {"request": request})

# Route: Handle form submission
@app.post("/submit", response_class=HTMLResponse)
async def handle_form(
    request: Request,
    username: str = Form(...),
    comment: str = Form(None),
    file: UploadFile = File(...)
):
    """
    Process submitted form and uploaded file.
    """
    file_location = f"uploads/{file.filename}"

    # Save uploaded file
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "username": username,
            "comment": comment,
            "filename": file.filename,
            "file_url": f"/uploads/{file.filename}"
        },
    )

# create template folder and put form and reult file in that folder
