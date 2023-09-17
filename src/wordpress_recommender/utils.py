import os
from wordpress_recommender.configs import DATA_LOC
from urllib.parse import urlparse
import logging
from typing import List
import pandas as pd

logger = logging.getLogger(__name__)


def get_content_file_path_for_sitemap(sitemap_url: str) -> str:
    file_name = urlparse(sitemap_url).netloc.replace(".", "_") + ".csv"
    logging.info(f"file_name: {file_name}")
    file_path = os.path.join(DATA_LOC, urlparse(sitemap_url).netloc.replace(".", "_") + ".csv")
    return file_path


def write_site_content_to_file(site_content: List[dict], sitemap_url: str):
    content_df = pd.DataFrame(site_content)
    file_path = get_content_file_path_for_sitemap(sitemap_url)
    content_df.to_csv(file_path, index=False)
