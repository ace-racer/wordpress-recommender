import os

DATA_LOC = os.getenv("DATA_LOC", "./data")
HF_KEY = os.getenv("HF_KEY")
DEFAULT_EMBEDDINGS_MODEL_NAME = os.getenv(
    "HF_EMBEDDINGS_MODEL_NAME", "sentence-transformers/all-MiniLM-l6-v2"
)

if not os.path.exists(DATA_LOC):
    os.makedirs(DATA_LOC)

if not HF_KEY:
    print("WARNING: HuggingFace inference API key is not provided as an environment variable")
