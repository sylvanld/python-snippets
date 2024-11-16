
.venv:
	virtualenv -p python3 .venv

##@ commands

help: ## Show this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make <COMMAND>\033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

install: .venv ## Install test requirements
	.venv/bin/pip install --index-url "" -e .[dev]
	.venv/bin/pip freeze --exclude-editable > requirements.lock.txt

main: ## Run main script
	.venv/bin/python main.py

clean: ## Clean code
	.venv/bin/isort main.py snippet/ tests/
	.venv/bin/black main.py snippet/ tests/
	find . | grep -E "(/__pycache__$$|\.pyc$$|\.pyo$$)" | xargs rm -rf
	rm -rf .pytest_cache/
