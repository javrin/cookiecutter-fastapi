PYTHON_VERSION ?= {{cookiecutter.python_version}}
SRC_DIR := src
CMD := poetry run
TESTS_DIR := tests

help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
.PHONY: help

format: ## rewrites code with black and isort
	$(CMD) black $(SRC_DIR) $(TESTS_DIR)
	$(CMD) isort $(SRC_DIR) $(TESTS_DIR)
.PHONY: format

lint-black: ## checks src and tests with black
	$(CMD) black --check --fast $(SRC_DIR) $(TESTS_DIR)
.PHONY: lint-black

lint-ruff: ## checks src and tests with ruff
	$(CMD) ruff check $(SRC_DIR) $(TESTS_DIR)
.PHONY: lint-ruff

lint-mypy: ## checks type annotation
	$(CMD) mypy $(SRC_DIR)
.PHONY: lint-mypy

lint: lint-black lint-ruff lint-mypy ## runs all static analysis tools
.PHONY: lint

test: ## runs tests
	$(CMD) pytest --cov=src --cov-report html:tests/.coverage $(TESTS_DIR)
.PHONY: test

safety: ## tests third party packages against a database of known compromised ones
	poetry export --with dev --format=requirements.txt --without-hashes | poetry run safety check --stdin

qa: safety lint test ## for CI/CD. Runs all code quality tools
.PHONY: qa

qa-local: format qa ## for local development (before checking in). Formats code and runs qa
.PHONY: qa-local

serve: ## runs the app
	docker compose -f docker-compose.yml up
.PHONY: serve

debug: ## runs the app in debug mode
	docker compose -f docker-compose-debug.yml up
.PHONY: debug
