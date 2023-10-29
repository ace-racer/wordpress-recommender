from typer.testing import CliRunner
import os


runner = CliRunner()

def test_download_content(test_sitemap_url, test_api_key):
    os.environ["HF_KEY"] = test_api_key
    from wordpress_recommender.main import app
    result = runner.invoke(app, ["download-content", test_sitemap_url])
    assert result.exit_code == 0

def test_build_index(test_sitemap_url, test_api_key):
    os.environ["HF_KEY"] = test_api_key
    from wordpress_recommender.main import app
    result = runner.invoke(app, ["build-index", test_sitemap_url, "--rebuild-index"])
    assert result.exit_code == 0


def test_query_index(test_sitemap_url, test_api_key):
    os.environ["HF_KEY"] = test_api_key
    from wordpress_recommender.main import app
    result = runner.invoke(app, ["query-index", test_sitemap_url, "--query", "Why is web crawling important?"])
    assert result.exit_code == 0
