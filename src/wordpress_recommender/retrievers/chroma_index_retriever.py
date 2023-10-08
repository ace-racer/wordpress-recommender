import os
from langchain.vectorstores import Chroma
from wordpress_recommender.common.embedding_utils import hf_inference_api_embeddings_model


def query_index(index_path: str, query: str, embeddings_model=hf_inference_api_embeddings_model):
    if not os.listdir(index_path):
        print(f"Index is not present. Please generate the index at {index_path} and try again!")
        return

    print(f"Querying Chroma index saved at {index_path}")

    # load DB from disk and find similar results to query
    db = Chroma(persist_directory=index_path, embedding_function=embeddings_model)
    docs = db.similarity_search(query)
    return docs
