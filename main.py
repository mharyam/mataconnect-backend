from fastapi import FastAPI

from app.interfaces.api import router

app = FastAPI()

# Include API routes
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to MataConnect API!"}
