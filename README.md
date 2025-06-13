<<<<<<< HEAD
# mataconnect-backend
=======
# MataConnect Backend

MataConnect is an AI-powered search engine that helps women discover relevant communities. This backend is built using FastAPI and follows Domain-Driven Design (DDD) principles.

## Features
- Accepts user queries to find relevant communities
- Uses Google Vertex AI for generating embeddings
- Performs vector search on MongoDB Atlas

## Project Structure
```
mataconnect-backend/
├── main.py                # Application entry point
├── app/
│   ├── core/              # App configuration and settings
│   ├── domain/            # Core business models
│   ├── application/       # Use cases and orchestrators
│   ├── infrastructure/    # External services (MongoDB, Vertex AI)
│   └── interfaces/        # API route handlers and schemas
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mataconnect-backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables in the `.env` file.

## Running the Application
Start the FastAPI server:
```bash
uvicorn main:app --reload
```

Access the API documentation at `http://127.0.0.1:8000/docs`.

## License
This project is licensed under the MIT License.
>>>>>>> dfa3ebc (Initial commit for mataconnect-backend)
