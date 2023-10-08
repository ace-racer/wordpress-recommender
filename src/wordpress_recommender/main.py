import typer
from wordpress_recommender.content_extractors.sitemap_content_extractor import get_site_content
from wordpress_recommender.utils import write_site_content_to_file
from wordpress_recommender.index_creators.chroma_index_creator import create_index
from wordpress_recommender.utils import (
    get_content_file_path_for_sitemap,
    get_index_path_for_sitemap,
)
from wordpress_recommender.retrievers.chroma_index_retriever import query_index
from enum import Enum

app = typer.Typer()


class Steps(str, Enum):
    download_content = "download-content"
    build_index = "build-index"
    query_index = "query-index"


@app.command()
def main(step: Steps, sitemap_url: str, query: str = ""):
    """
    An application to recommend articles from a Wordpress blog based on user's query using semantic search
    """
    if step == Steps.download_content:
        print(f"Downloading content from sitemap: {sitemap_url}")
        site_content = get_site_content(sitemap_url)

        print("Writing downloaded content to file")
        write_site_content_to_file(site_content, sitemap_url)

        print("Finished downloading content...")
    elif step == Steps.build_index:
        print(f"Reading downloaded content: {sitemap_url}")
        content_file_path = get_content_file_path_for_sitemap(sitemap_url)
        print("Generating index")
        index_path = get_index_path_for_sitemap(sitemap_url)
        create_index(content_file_path, index_path)
        print("Finished index creation...")
    elif step == Steps.query_index:
        print(f"Generating results for query: {query}")
        index_file_path = get_index_path_for_sitemap(sitemap_url)

        print("Generating results")
        docs = query_index(index_file_path, query)
        print(f"Retrieved {len(docs)} results for query")
        print("Most relevant result details...")
        print(f"URL: {docs[0].metadata['source']}")
        print(f"Content: {docs[0].page_content}")
        return docs
    else:
        print(f"Invalid step chosen: {step}")


if __name__ == "__main__":
    typer.run(main)
