from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import api_router

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://mataconnect-website-bkxslbfewa-nw.a.run.app/",
        "http://mataconnect.org/",
        "https://mataconnect-website.vercel.app/",
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Register all API routes under /api
app.include_router(api_router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Welcome to MataConnect API!"}
