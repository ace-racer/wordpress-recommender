import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def test_sitemap_url():
    return os.environ["SITEMAP_URL"]

@pytest.fixture
def test_api_key():
    return os.environ["HF_KEY"]
