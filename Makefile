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
	