from setuptools import setup


setup(name='mlpro_int_openml',
version='1.0.0',
description='MLPro: Integration OpenML',
author='MLPro Team',
author_mail='mlpro@listen.fh-swf.de',
license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
packages=['mlpro_int_openml'],

# Package dependencies for full installation
extras_require={
    "full": [
        "dill",
        "numpy",
        "matplotlib",
        "multiprocess",
        "mlpro"
    ],
},

zip_safe=False)