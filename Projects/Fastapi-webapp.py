from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"this is our first web app "}