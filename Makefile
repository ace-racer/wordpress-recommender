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
	@poetry run python src/wordpress_recommender/main.py download-content "$(sitemap_url)"

generate-index:
	@poetry run python src/wordpress_recommender/main.py build-index "$(sitemap_url)" --rebuild-index

query-index:
	@poetry run python src/wordpress_recommender/main.py query-index "$(sitemap_url)" --query "$(query)" --top $(top)


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
	