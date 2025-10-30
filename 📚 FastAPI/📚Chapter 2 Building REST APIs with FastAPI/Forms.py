from fastapi import FastAPI, Form

app = FastAPI(title="Form Handling Example")

@app.post("/submit-form")
async def submit_form(
    username: str = Form(...),
    email: str = Form(...),
    feedback: str = Form(None)
):
    """
    Handle form submissions from users.
    """
    return {
        "message": "Form data received!",
        "user": username,
        "email": email,
        "feedback": feedback or "No feedback provided"
    }

