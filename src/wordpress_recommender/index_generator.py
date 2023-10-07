from wordpress_recommender.index_creators.chroma_index_creator import create_index
from wordpress_recommender.utils import get_content_file_path_for_sitemap, get_index_path_for_sitemap
import fire
import sys


def main(sitemap_url: str):
    print(f"Reading downloaded content: {sitemap_url}")
    content_file_path = get_content_file_path_for_sitemap(sitemap_url)

    print("Generating index")
    index_path = get_index_path_for_sitemap(sitemap_url)
    create_index(content_file_path, index_path)

    print("Finished index creation...")


if __name__ == "__main__":
    fire.Fire(main)
    sys.exit(0)
