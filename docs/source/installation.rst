.. highlight:: shell

============
Installation
============


Stable release
--------------

To install ``ezqueue``, run this command in your terminal:

.. code-block:: console

    $ pip install ezqueue

This is the preferred method to install ``ezqueue``, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The source for ``ezqueue`` can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/jwcnewton/ezqueue

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/jwcnewton/ezqueue/tarball/main

Once you have a copy of the source, you can install it. The method of installation will depend on the packaging library being used.

For example, if `setuptools`_ is being used (a ``setup.py`` file is present), install ``ezqueue`` with:

.. code-block:: console

    $ python setup.py install

If `poetry`_ is being used (``poetry.lock`` and ``pyproject.toml`` files are present), install ``ezqueue`` with:

.. code-block:: console

    $ poetry install


.. _Github repo: https://github.com/jwcnewton/ezqueue
.. _tarball: https://github.com/jwcnewton/ezqueue/tarball/master
.. _poetry: https://python-poetry.org
.. _setuptools: https://setuptools.readthedocs.io/en/latest/
