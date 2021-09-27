===========
EXAMPLE_PKG
===========

Just an example package to prove a point ;)

The purpose of this project is to provide starting point to test Sphinx API documentation generation using `autodoc` for a package with native namespaces more than one level deep.

Project setup
=============

.. code-block::

    setup.py
    setup.cfg
    docs/
    example_pkg/
        # No __init__.py here.
        middle_package/
            # No __init__.py here.
            subpackage_a/
                # Sub-packages have __init__.py.
                __init__.py
                test_a.py

Building documentation
======================

.. code-block::

    make docs-preview

this make command is just the combination of the following commands:

.. code-block::

    # install package as development
    python -m pip install -e .

    # invoke the Sphinx autodoc extension
    sphinx-apidoc --implicit-namespaces --force -o docs/ ./src/

    # clean docs and invoke Sphinx html generation
    make -C docs clean
    make -C docs html

    # open the webbrowser
    python -m webbrowser docs/_build/html/index.html