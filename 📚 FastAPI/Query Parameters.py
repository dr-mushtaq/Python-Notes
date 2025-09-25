from fastapi import FastAPI

app = FastAPI()

# Define query parameters
@app.get("/products/")
def read_products(category: str = None, limit: int = 10):
    return {"category": category, "limit": limit}

