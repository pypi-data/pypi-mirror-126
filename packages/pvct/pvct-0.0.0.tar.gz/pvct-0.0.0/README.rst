========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |requires|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/pvct/badge/?style=flat
    :target: https://pvct.readthedocs.io/
    :alt: Documentation Status

.. |requires| image:: https://requires.io/github/rowlesmr/pvct/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/rowlesmr/pvct/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/pvct.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pvct

.. |wheel| image:: https://img.shields.io/pypi/wheel/pvct.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pvct

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pvct.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pvct

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pvct.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pvct

.. |commits-since| image:: https://img.shields.io/github/commits-since/rowlesmr/pvct/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/rowlesmr/pvct/compare/v0.0.0...master



.. end-badges

A program to construct a pseudo-variable count time diffraction pattern from many fixed-time diffraction patterns.

* Free software: Apache Software License 2.0

Installation
============

::

    pip install pvct

You can also install the in-development version with::

    pip install https://github.com/rowlesmr/pvct/archive/master.zip


Documentation
=============


https://pvct.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
