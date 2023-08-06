# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hostfact_python_client']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0', 'vcrpy>=4.1.1,<5.0.0']

setup_kwargs = {
    'name': 'hostfact-python-client',
    'version': '0.1.3',
    'description': '',
    'long_description': None,
    'author': 'Kamenlom',
    'author_email': 'ivashchenko.roman111@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
