import sys
from setuptools import setup

packages = ['root.a']

if sys.version_info.major == 2:
    packages += ['root']

setup(
    name='root-a',
    version='0.1',
    description='Namespace package one level below root.',
    author='Radomir Stevanovic',
    author_email='radomir@dwavesys.com',
    packages=packages,
    zip_safe=False,
)
