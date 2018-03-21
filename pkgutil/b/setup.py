import sys
from setuptools import setup

packages = ['root.b']

if sys.version_info.major == 2:
    packages += ['root']

setup(
    name='root-b',
    version='0.1',
    description='Namespace package one level below root.',
    author='Radomir Stevanovic',
    author_email='radomir@dwavesys.com',
    packages=packages,
    zip_safe=False,
)
