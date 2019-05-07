.PHONY: test lint

test:
	py.test --cov=getalltweets tests/
lint:
	pylint getalltweets/
