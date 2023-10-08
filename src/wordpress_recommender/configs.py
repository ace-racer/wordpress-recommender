import os

DATA_LOC = os.getenv("DATA_LOC", "./data")
HF_KEY = os.getenv("HF_KEY")

if not os.path.exists(DATA_LOC):
    os.makedirs(DATA_LOC)

if not HF_KEY:
    print("WARNING: HuggingFace inference API key is not provided as an environment variable")
