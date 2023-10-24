DOCKER_IMAGE_NAME := api-salsa
IMAGE_VERSION := 1.0

start: ## cria ambiente virtual com poetry e instala bibliotecas de dev
	git init 
	poetry init -n
	poetry add --group dev blue
	poetry add --group dev isort
	poetry add --group dev pytest
	poetry add --group dev pytest-cov
	poetry add --group dev ipython
	mkdir tests
	echo "" > tests/__init__.py
	echo __pycache__/ > .gitignore
	echo pass.env >> .gitignore
	echo .pytest_cache/ >> .gitignore
	poetry add --group doc mkdocs-material
	poetry add --group doc mkdocstrings
	poetry add --group doc mkdocstrings-python
	mkdir docs
	mkdir code
	echo "" > code/__init__.py

format: ## formata o script e ordena os imports
	poetry run blue .
	poetry run isort .
	poetry run prospector

dev: ## Start Container em modo iterativo
	poetry run ipython -i code/main.py

git: ## MSG - Sobe codigo pro GIT (Necessario usar variavel)
	git add -A
	git commit -m "${MSG}"
	git push -u origin main