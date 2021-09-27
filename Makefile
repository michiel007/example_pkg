.PHONY: docs-preview

ALL: docs-preview

clean:  ## clean project space
	$(MAKE) -C docs clean
	python -m pip uninstall -y example-pkg
	rm -f docs/example_package.rst
	rm -f docs/example_package.*.rst
	rm -f docs/modules.rst
	rm -fr docs/_build/
	rm -fr .eggs/
	-find . -name '*.egg-info' -exec rm -fr {} +
	-find . -name '*.egg' -exec rm -f {} +
	-find . -name '*.pyc' -exec rm -f {} +
	-find . -name '*.pyo' -exec rm -f {} +
	-find . -name '*~' -exec rm -f {} +
	-find . -name '__pycache__' -exec rm -fr {} +

docs-preview: clean ## generate and show Sphinx HTML documentation, including API docs
	python -m pip install -e .
	sphinx-apidoc --implicit-namespaces --force -o docs/ ./example_package/
	$(MAKE) -C docs html
	python -m webbrowser docs/_build/html/index.html
