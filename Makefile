PACKAGE=sse_bot

venv: requirements.txt requirements-dev.txt
	virtualenv venv
	./venv/bin/pip install -r requirements-dev.txt

.PHONY: test
test: venv
	./venv/bin/black $(PACKAGE)
	./venv/bin/tox

.PHONY: build
build: venv setup.py setup.cfg $(PACKAGE)
	./venv/bin/python setup.py sdist bdist_wheel

clean:
	rm -rf __pycache__
	rm -rf .tox
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf venv
	find . -iname '*.pyc' -exec rm {} \;
