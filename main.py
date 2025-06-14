from fastapi import FastAPI


from app.routes import api_router

app = FastAPI()


# Register all API routes under /api
app.include_router(api_router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Welcome to MataConnect API!"}
