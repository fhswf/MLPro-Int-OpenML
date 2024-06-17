.. MLPro Documentations documentation master file, created by
   sphinx-quickstart on Wed Sep 15 12:06:53 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MLPro-Int-OpenML - Integration of OpenML into MLPro
===================================================

Welcome to MLPro-Int-OpenML, an extension to MLPro to integrate the scientific data provider OpenML.
MLPro is a middleware framework for standardized machine learning in Python. It is 
developed by the South Westphalia University of Applied Sciences, Germany, and provides 
standards, templates, and processes for hybrid machine learning applications. OpenML, in turn, 
provides a vast amount of sample datasets, combined with a benchmark systematics to
enable a standardized assessment of ML algorithms.

MLPro-Int-OpenML provides wrapper classes that enable the use of OpenML datasets in your 
MLPro applications. The use of these wrappers is illustrated in example programs.

**Preparation**

Before running the examples, please install the latest versions of MLPro, OpenML, and MLPro-Int-OpenML as follows:

.. code-block:: bash

   pip install mlpro-int-openml[full] --upgrade


**See also**
   - `MLPro - Machine Learning Professional <https://mlpro.readthedocs.io>`_ 
   - `MLPro-OA - Sub-framework for online machine learning <https://mlpro.readthedocs.io/en/latest/content/03_machine_learning/mlpro_oa/main.html>`_
   - `OpenML - A worldwide machine learning lab <https://www.openml.org/>`_      
   - `Further MLPro extensions <https://mlpro.readthedocs.io/en/latest/content/04_extensions/main.html>`_
   - `MLPro-Int-OpenML on GitHub <https://github.com/fhswf/MLPro-Int-OpenML>`_


.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Home

   self


.. toctree::
   :maxdepth: 2
   :caption: Example Pool
   :glob:

   content/01_example_pool/*


.. toctree::
   :maxdepth: 2
   :caption: API Reference
   :glob:

   content/02_api/*


.. toctree::
   :maxdepth: 2
   :caption: About
   :glob:

   content/03_about/*
