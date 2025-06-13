from google.cloud import aiplatform
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

GCP_PROJECT = os.getenv("GCP_PROJECT")
GCP_REGION = os.getenv("GCP_REGION", "us-central1")
GCP_MODEL_NAME = os.getenv("GCP_MODEL_NAME", "textembedding-gecko@001")


def generate_embedding(text: str) -> List[float]:
    """Generate embedding for a given text using Vertex AI."""
    aiplatform.init(project=GCP_PROJECT, location=GCP_REGION)
    model = aiplatform.TextEmbeddingModel.from_pretrained(GCP_MODEL_NAME)
    response = model.get_embeddings([text])
    return response[0].values
