import typer
from wordpress_recommender.content_extractors.sitemap_content_extractor import get_site_content
from wordpress_recommender.utils import write_site_content_to_file
from wordpress_recommender.index_creators.chroma_index_creator import create_index
from wordpress_recommender.utils import (
    get_content_file_path_for_sitemap,
    get_index_path_for_sitemap,
    get_final_result_set,
)
from wordpress_recommender.retrievers.chroma_index_retriever import (
    query_index,
    RETRIEVAL_SCORE_FIELD_NAME,
)
from enum import Enum

app = typer.Typer()


class Steps(str, Enum):
    download_content = "download-content"
    build_index = "build-index"
    query_index = "query-index"


@app.command()
def main(step: Steps, sitemap_url: str, rebuild_index: bool = False, query: str = "", top: int = 5):
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
        create_index(content_file_path, index_path, rebuild_index)
        print("Finished index creation...")
    elif step == Steps.query_index:
        print(f"Generating results for query: {query}")
        index_file_path = get_index_path_for_sitemap(sitemap_url)

        print("Generating results")
        docs = query_index(index_file_path, query, top)
        result_df = get_final_result_set(sitemap_url, docs, RETRIEVAL_SCORE_FIELD_NAME)
        print(f"Final results:\n{result_df}")
        return result_df
    else:
        print(f"Invalid step chosen: {step}")


if __name__ == "__main__":
    typer.run(main)
