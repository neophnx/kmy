
PYLINT:=python3.12 -m pylint --rcfile pylint.toml

.PHONY: lint test

lint:
	black .
	mypy --strict kmy
	mypy tests
	${PYLINT} kmy tests


test:
	PYTHONPATH="." pytest --verbose --cov-branch --cov kmy tests