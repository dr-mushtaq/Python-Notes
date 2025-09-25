from fastapi import FastAPI

app = FastAPI()

# Define a path parameter
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

# http://127.0.0.1:8000/users/123



