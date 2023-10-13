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
    file_path = os.path.join(DATA_LOC, file_name)
    return file_path


def write_site_content_to_file(site_content: List[dict], sitemap_url: str):
    content_df = pd.DataFrame(site_content)
    file_path = get_content_file_path_for_sitemap(sitemap_url)
    content_df.to_csv(file_path, index=False)


def get_index_path_for_sitemap(sitemap_url: str) -> str:
    folder_name = urlparse(sitemap_url).netloc.replace(".", "_")
    logging.info(f"folder_name: {folder_name}")
    folder_path = os.path.join(DATA_LOC, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


def get_site_content_from_file(sitemap_url: str) -> pd.DataFrame:
    file_path = get_content_file_path_for_sitemap(sitemap_url)
    return pd.read_csv(file_path)


def get_final_result_set(sitemap_url: str, docs, retriever_score_field_name: str):
    content_df = get_site_content_from_file(sitemap_url)
    results = []
    for doc, score in docs:
        print(f"score: {score}")
        results.append({"url": doc.metadata["source"], retriever_score_field_name: score})

    results_df = pd.DataFrame(results)
    merged_df = pd.merge(content_df, results_df, on="url", how="inner")
    if "distance" in retriever_score_field_name:
        return merged_df.sort_values(by=[retriever_score_field_name])
    else:
        return merged_df.sort_values(by=[retriever_score_field_name], ascending=False)
