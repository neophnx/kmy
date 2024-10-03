

.PHONY: lint test

lint:
	black .
	mypy --strict kmy
	mypy tests


test:
	PYTHONPATH="." pytest --cov-branch --cov kmy tests