import requests
from bs4 import BeautifulSoup
import logging
import sys
import fire

logger = logging.getLogger(__name__)


def get_site_content(sitemap_url: str):
    if not sitemap_url.endswith(".xml"):
        raise ValueError(f"Provided sitemap {sitemap_url} is not valid sitemap url")

    # Send a GET request to the sitemap URL
    response = requests.get(sitemap_url)

    response.raise_for_status()

    # Check if the request was successful
    if response.status_code == 200:
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

                # Extract the date (you will need to modify this based on the structure of your page)
                # date = page_soup.find('lastmod').text if page_soup.find('lastmod') else None

                # Extract content (cleaned)
                content = ""
                for paragraph in page_soup.find_all("p"):
                    content += paragraph.get_text() + "\n"

                # Now, you can process the 'url', 'date', and 'content' as per your requirements
                # For example, you can save them to a file or a database, or perform further processing

                print("URL:", url)
                print(f"title: {title}")
                # print('Date:', date)
                # Print or save the content as needed
                print(
                    "Content:", content[:1000]
                )  # Print the first 100 characters for demonstration
                print("-" * 50)

            else:
                logger.error(f"Failed to fetch page URL: {url}")


if __name__ == "__main__":
    fire.Fire(get_site_content)
    sys.exit(0)
