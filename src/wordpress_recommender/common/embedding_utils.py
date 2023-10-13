from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from wordpress_recommender.configs import HF_KEY, DEFAULT_EMBEDDINGS_MODEL_NAME


# TODO: Can try different models and libraries
hf_inference_api_embeddings_model = HuggingFaceInferenceAPIEmbeddings(
    api_key=HF_KEY, model_name=DEFAULT_EMBEDDINGS_MODEL_NAME
)
