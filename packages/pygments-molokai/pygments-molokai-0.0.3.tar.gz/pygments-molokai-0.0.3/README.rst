=======================
Pygments Molokai Plugin
=======================

This Python package can be used to add the Molokai colour theme to Pygments.  It was generated from the `Vim Molokai plugin`_ using the `Vim Colorscheme Converter`_.  Once installed, a Pygments style named 'molokai' will become available.

.. image:: https://raw.githubusercontent.com/gbpoole/gbpoole.github.io/main/assets/screen_shots/pygments_molokai_screen_shot.png
  :alt: Pygments Molokai Screen Shot
  :align: center

.. _`Vim Molokai plugin`: https://github.com/tomasr/molokai

.. _`Vim Colorscheme Converter`: https://github.com/honza/vim2pygments

Install
=======

With Pygments installed, the Molokai style can be added as follows:

Using PyPI and pip
------------------

The easiest way is to use 'pip':
::

    $ pip install pygments-molokai


Manual
------

For those who want to work from code, you can install the Molokai theme manually.  First make sure that Poetry is installed (see `here`).  Then:
::

    $ git clone git://github.com/gbpoole/pygments-molokai.git
    $ cd pygments-molokai
    $ poetry install

.. _here: https://python-poetry.org/docs/#installation

Usage examples
==============

From Python:
::

    >>> from pygments.formatters import HtmlFormatter
    >>> HtmlFormatter(style='molokai').style
    <class 'pygments_style_molokai.MolokaiStyle'>


or from the command line:
::

    pygmentize -g -O style=molokai <FILENAME>

Help
====

More information about Pygment styles can be found at the `official Pygments documentation`_ page.

.. _official Pygments documentation: https://pygments.org/docs/styles/

