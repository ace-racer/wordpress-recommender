import os
from langchain.vectorstores import Chroma
from wordpress_recommender.common.embedding_utils import hf_inference_api_embeddings_model
import pandas as pd

RETRIEVAL_SCORE_FIELD_NAME = "cosine_distance"


def query_index(
    index_path: str, query: str, top: int, embeddings_model=hf_inference_api_embeddings_model
) -> pd.DataFrame:
    if not os.listdir(index_path):
        print(f"Index is not present. Please generate the index at {index_path} and try again!")
        return

    print(f"Querying Chroma index saved at {index_path}")

    # load DB from disk and find similar results to query
    db = Chroma(persist_directory=index_path, embedding_function=embeddings_model)

    # The returned distance score is cosine distance. Therefore, a lower score is better.
    docs = db.similarity_search_with_score(query, k=top)
    return docs
