import requests
from bs4 import BeautifulSoup
import logging
from typing import List
from tqdm import tqdm

logger = logging.getLogger(__name__)


def get_site_content(sitemap_url: str) -> List[dict]:
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
        filtered_locs = [loc for loc in locs if loc.prefix == ""]
        print(f"Total content pages to download: {len(filtered_locs)}")

        for loc in tqdm(filtered_locs, desc="Downloading content from blog..."):
            logger.info(f"loc: {dir(loc)} prefix: {loc.prefix}")

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

            else:
                logger.error(f"Failed to fetch page URL: {url}")
        return site_content
    else:
        logger.error(f"Could not parse the sitemap: {sitemap_url}")
    return []
