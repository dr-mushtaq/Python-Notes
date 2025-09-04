# main.py
from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Define a simple GET endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


