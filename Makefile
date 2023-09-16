lint-check: 
	@poetry run ruff check src/

lint-fix:
	@poetry run ruff --fix src/

format-check:
	@poetry run black --check --diff src/

format-fix:
	@poetry run black src/


complete-check: lint-check format-check
complete-fix: lint-fix format-fix