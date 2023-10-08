from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from wordpress_recommender.configs import HF_KEY


# TODO: Can try different models and libraries
hf_inference_api_embeddings_model = HuggingFaceInferenceAPIEmbeddings(
    api_key=HF_KEY, model_name="sentence-transformers/all-MiniLM-l6-v2"
)
