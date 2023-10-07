from langchain.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
import os
from langchain.vectorstores import Chroma

HF_KEY = os.getenv("HF_KEY")

# TODO: Can try different models and libraries
embeddings_model = HuggingFaceInferenceAPIEmbeddings(
    api_key=HF_KEY,
    model_name="sentence-transformers/all-MiniLM-l6-v2"
)

# TODO: Can try different text splitters
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap  = 100,
    length_function = len,
    add_start_index = True,
)

def create_index(site_content_path: str, index_path: str):
    if os.listdir(index_path):
        print(f"Index is already generated. Please delete the folder {index_path} and try again!")
        return

    print(f"Creating Chroma index and saving at {index_path}")
    loader = CSVLoader(file_path=site_content_path,
    source_column="url")

    docs = loader.load()
    print(f"Read {len(docs)} pages from site content saved in: {site_content_path}")

    # load it into Chroma
    Chroma.from_documents(docs, embeddings_model, persist_directory=index_path)

