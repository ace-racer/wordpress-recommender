import os
from langchain.vectorstores import Chroma
from wordpress_recommender.index_creators.chroma_index_creator import embeddings_model

def query_index(index_path: str, query: str):
    if not os.listdir(index_path):
        print(f"Index is not present. Please generate the index at {index_path} and try again!")
        return

    print(f"Querying Chroma index saved at {index_path}")

    # load DB from disk
    db = Chroma(persist_directory=index_path, embedding_function=embeddings_model)
    docs = db.similarity_search(query)
    return docs
