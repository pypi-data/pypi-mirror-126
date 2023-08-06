
ethosdistro_py
----------------
.. image:: https://github.com/CoryKrol/ethosdistro_py/workflows/CI/badge.svg?branch=master
     :target: https://github.com/CoryKrol/ethosdistro_py/actions?workflow=CI
     :alt: CI Status

A Python wrapper for the EthOS REST API

Installation
------------
Install with pip:

.. code-block:: bash

   pip install ethosdistro_py

Usage
------------

.. code-block:: python

   from ethos_py import EthosAPI

   session = aiohttp.ClientSession()
   ethosapi = EthosAPI(session=session)


Configuration
-------------------

Environment File
--------------------------------
.. code-block::

   ETHOS_PANEL_ID=<api_key>


References
------------

Contribute
----------

- `Issue Tracker <https://github.com/CoryKrol/ethosdistro_py/issues>`_
- `Source Code <https://github.com/CoryKrol/ethosdistro_py>`_

Support
-------

`Open an issue <https://github.com/CoryKrol/ethosdistro_py/issues/new>`_

License
-------

The project is licensed under the Apache 2 license