from __future__ import absolute_import

from distutils.core import setup
from setuptools import find_packages


setup(
    name='babysitter',
    version='1.0.0',
    description='Babysitter - Free issue tracking',
    author='Alexandru Mihai',
    author_email='92.alexandru.mihai@gmail.com',
    packages=find_packages('src'),
    package_dir={'babysitter': 'src/babysitter'},
    include_package_data=True,
    install_requires=[
        'tornado>=4.2.1',
    ],
)

