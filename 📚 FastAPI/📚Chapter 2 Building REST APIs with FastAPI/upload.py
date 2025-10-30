from fastapi import FastAPI, File, UploadFile

app = FastAPI(title="File Upload Example")

@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    """
    Accept a single file upload from the client.
    """
    # Read file contents
    contents = await file.read()

    # Optionally, save the file
    with open(file.filename, "wb") as f:
        f.write(contents)

    return {"filename": file.filename, "content_type": file.content_type}

