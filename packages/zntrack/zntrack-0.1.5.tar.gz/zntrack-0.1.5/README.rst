|build| |docs| |license| |code style|

.. image:: https://raw.githubusercontent.com/zincware/ZnTrack/main/docs/source/img/zntrack.png

Object-Relational Mapping for DVC
---------------------------------

The ZnTrack [zɪŋk træk] package provides a Python ORM for DVC.

For more information on DVC visit their `homepage <https://dvc.org/doc>`_.

Example
========
ZnTrack allows you to convert most Python classes into a DVC stage, including
parameters, dependencies and all DVC output types.

.. code-block:: py

    from zntrack import Node, dvc
    from random import randrange


    @Node()
    class HelloWorld:
        """Define a ZnTrack Node"""
        # parameter to be tracked
        max_number = dvc.params()
        # parameter to store as output
        random_number = dvc.result()

        def __call__(self, max_number):
            """Pass tracked arguments"""
            self.max_number = max_number

        def run(self):
            """Command to be run by DVC"""
            self.random_number = randrange(self.max_number)

This stage can be used via

.. code-block:: py

    hello_world = HelloWorld()
    hello_world(max_number=512)

which builds the DVC stage and can be used e.g., through :code:`dvc repro`.
The results can then be accessed easily via :code:`HelloWorld(load=True).random_number`.

More detailed examples and further information can be found in the `ZnTrack Documentation <https://zntrack.readthedocs.io/en/latest/>`_.


Installation
============

Simply run:

.. code-block:: bash

   pip install zntrack

Or you can install from source with:

.. code-block:: bash

   git clone https://github.com/zincware/ZnTrack.git
   cd ZnTrack
   pip install .

.. badges

.. |build| image:: https://github.com/zincware/ZnTrack/actions/workflows/pytest.yaml/badge.svg
    :alt: Build tests passing
    :target: https://github.com/zincware/py-test/blob/readme_badges/

.. |docs|  image:: https://readthedocs.org/projects/zntrack/badge/?version=latest
    :target: https://zntrack.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |license| image:: https://img.shields.io/badge/License-EPL-purple.svg?style=flat
    :alt: Project license
    :target: https://www.eclipse.org/legal/epl-2.0/faq.php

.. |code style| image:: https://img.shields.io/badge/code%20style-black-black
    :alt: Code style: black
    :target: https://github.com/psf/black/
