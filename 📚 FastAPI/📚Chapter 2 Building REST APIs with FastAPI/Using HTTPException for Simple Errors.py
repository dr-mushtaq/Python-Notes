# error_handling_fastapi.py
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Example route: get user by ID
users = {"1": "Alice", "2": "Bob", "3": "Charlie"}

@app.get("/users/{user_id}")
def get_user(user_id: str):
    if user_id not in users:
        # Raise a 404 error if user not found
        raise HTTPException(
            status_code=404,
            detail=f"User with ID {user_id} not found."
        )
    return {"user_id": user_id, "name": users[user_id]}

