from wordpress_recommender.content_extractors.sitemap_content_extractor import get_site_content
from wordpress_recommender.utils import write_site_content_to_file
import fire
import sys


def main(sitemap_url: str):
    print(f"Downloading content from sitemap: {sitemap_url}")
    site_content = get_site_content(sitemap_url)

    print("Writing downloaded content to file")
    write_site_content_to_file(site_content, sitemap_url)

    print("Finished...")


if __name__ == "__main__":
    fire.Fire(main)
    sys.exit(0)
