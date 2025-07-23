from setuptools import setup


setup(name='mlpro-int-openml',
version='1.1.0',
description='MLPro: Integration OpenML',
author='MLPro Team',
author_mail='mlpro@listen.fh-swf.de',
license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
packages=['mlpro_int_openml'],

# Package dependencies for full installation
extras_require={
    "full": [
        "mlpro[full]>=2.1.0",
        "openml>=0.15.1"
    ],
},

zip_safe=False)