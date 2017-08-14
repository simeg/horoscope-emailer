.PHONY: ci install test

ci: install lint test

install:
	pip install -r requirements.txt

lint:
	pep8 --format=pylint src test

test:
	pytest
