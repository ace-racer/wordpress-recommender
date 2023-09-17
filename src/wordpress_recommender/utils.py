import os
from wordpress_recommender.configs import DATA_LOC
from urllib.parse import urlparse
import logging

logger = logging.getLogger(__name__)

def get_content_file_path_for_sitemap(sitemap_url: str) -> str:
    file_name = urlparse(sitemap_url).netloc.replace(".", "_") + ".csv"
    logging.info(f"file_name: {file_name}")
    file_path = os.path.join(DATA_LOC, urlparse(sitemap_url).netloc.replace(".", "_") + ".csv")
    return file_path
