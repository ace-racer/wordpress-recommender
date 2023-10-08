from langchain.document_loaders.csv_loader import CSVLoader

from wordpress_recommender.common.embedding_utils import hf_inference_api_embeddings_model
import os
from langchain.vectorstores import Chroma


def create_index(
    site_content_path: str, index_path: str, embeddings_model=hf_inference_api_embeddings_model
):
    if os.listdir(index_path):
        print(f"Index is already generated. Please delete the folder {index_path} and try again!")
        return

    print(f"Creating Chroma index and saving at {index_path}")
    loader = CSVLoader(file_path=site_content_path, source_column="url")

    docs = loader.load()
    print(f"Read {len(docs)} pages from site content saved in: {site_content_path}")

    # load it into Chroma
    Chroma.from_documents(docs, embeddings_model, persist_directory=index_path)
