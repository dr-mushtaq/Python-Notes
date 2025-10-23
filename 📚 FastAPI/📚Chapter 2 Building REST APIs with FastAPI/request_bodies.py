# Import necessary modules
from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI instance
app = FastAPI()

# Define a Pydantic model for request body validation
class User(BaseModel):
    name: str
    email: str
    age: int

# Create a POST endpoint that accepts JSON data
@app.post("/create-user/")
def create_user(user: User):
    """
    This endpoint receives a user object,
    automatically validates it, and returns a response.
    """
    return {
        "message": f"User {user.name} successfully created!",
        "user_data": user
    }

# http://127.0.0.1:8000/docs
# You’ll see an interactive Swagger UI where you can send test requests without writing any frontend code.
# Once you run the app (uvicorn main:app --reload), open your browser at:
