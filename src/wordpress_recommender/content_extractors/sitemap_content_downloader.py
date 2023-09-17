import requests
from bs4 import BeautifulSoup
import logging
import sys
import fire
import pandas as pd
from wordpress_recommender.utils import get_content_file_path_for_sitemap

logger = logging.getLogger(__name__)


def get_site_content(sitemap_url: str):
    if not sitemap_url.endswith(".xml"):
        raise ValueError(f"Provided sitemap {sitemap_url} is not valid sitemap url")

    # Send a GET request to the sitemap URL
    response = requests.get(sitemap_url)

    response.raise_for_status()

    # Check if the request was successful
    if response.status_code == 200:
        site_content = []

        # Parse the sitemap XML using BeautifulSoup
        soup = BeautifulSoup(response.text, "xml")

        # Extract URLs from the sitemap
        locs = soup.find_all("loc")

        for loc in locs:
            logger.info(f"loc: {dir(loc)} prefix: {loc.prefix}")

            if loc.prefix != "":
                logger.warning(f"Invalid tag prefix [{loc.prefix}]...")
                continue

            # Extract the URL
            url = loc.text

            logger.info(f"post url: {url}")

            # Send a GET request to the page URL
            page_response = requests.get(url)

            # Check if the request to the page was successful
            if page_response.status_code == 200:
                # Parse the page content using BeautifulSoup
                page_soup = BeautifulSoup(page_response.text, "html.parser")

                # Extract title
                title = page_soup.title.string if page_soup.title else ""

                # Extract content
                content = ""
                for paragraph in page_soup.find_all("p"):
                    content += paragraph.get_text() + "\n"

                date = page_soup.find("time").contents[0] if page_soup.find("time") else ""
                site_content.append(
                    {
                        "url": url,
                        "title": title,
                        "date": date,
                        "content": content,
                    }
                )

                print("-" * 50)

            else:
                logger.error(f"Failed to fetch page URL: {url}")
        content_df = pd.DataFrame(site_content)
        file_path = get_content_file_path_for_sitemap(sitemap_url)
        content_df.to_csv(file_path, index=False)

    else:
        logger.error(f"Could not parse the sitemap: {sitemap_url}")



if __name__ == "__main__":
    fire.Fire(get_site_content)
    sys.exit(0)
