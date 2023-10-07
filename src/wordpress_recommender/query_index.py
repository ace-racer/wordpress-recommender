from wordpress_recommender.retrievers.chroma_index_retriever import query_index
from wordpress_recommender.utils import get_index_path_for_sitemap
import fire
import sys


def main(sitemap_url: str, query: str):
    print(f"Generating results for query: {query}")
    index_file_path = get_index_path_for_sitemap(sitemap_url)

    print("Generating results")
    docs = query_index(index_file_path, query)
    print(f"Retrieved {len(docs)} results for query")
    print("Most relevant result details...")
    print(f"URL: {docs[0].metadata['source']}")
    print(f"Content: {docs[0].page_content}")


if __name__ == "__main__":
    fire.Fire(main)
    sys.exit(0)
