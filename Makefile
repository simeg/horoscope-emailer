.PHONY: ci deploy install lint test

ci: install lint test

deploy:
	git push heroku master

install:
	pip install -r requirements.txt

lint:
	pep8 --format=pylint src test

test:
	pytest
