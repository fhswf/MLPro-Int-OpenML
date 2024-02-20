from setuptools import setup


setup(name='mlpro-int-openml',
version='0.1.0',
description='MLPro: Integration OpenML',
author='MLPro Team',
author_mail='mlpro@listen.fh-swf.de',
license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
packages=['mlpro_int_openml'],

# Package dependencies for full installation
extras_require={
    "full": [
        "mlpro[full]>=1.3.1",
        "openml>=0.14.2"
    ],
},

zip_safe=False)