# Default target executed when no arguments are given to make.
all: help

lint-check: 
	@poetry run ruff check src/

lint-fix:
	@poetry run ruff --fix src/

format-check:
	@poetry run black --check --diff src/

format-fix:
	@poetry run black src/

download-content:
	@poetry run python src/wordpress_recommender/content_downloader.py --sitemap_url "$(sitemap_url)"

generate-index:
	@poetry run python src/wordpress_recommender/index_generator.py --sitemap_url "$(sitemap_url)"

query-index:
	@poetry run python src/wordpress_recommender/query_index.py --sitemap_url "$(sitemap_url)" --query "$(query)"


complete-check: lint-check format-check
complete-fix: lint-fix format-fix


######################
# HELP
######################

help:
	@echo '----'
	@echo 'complete-check               - run lint-check and format-check'
	@echo 'complete-fix                 - run lint-fix and format-fix'
	@echo 'download-content             - run download-content'
	@echo 'generate-index             	- run generate-index'
	@echo 'query-index             		- run query-index'
	