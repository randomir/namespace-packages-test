import sys
from setuptools import setup

packages = ['root.b.c']

if sys.version_info.major == 2:
    packages += ['root', 'root.b']

setup(
    name='root-b-c',
    version='0.1',
    description='Namespace package two levels below root.',
    author='Radomir Stevanovic',
    author_email='radomir@dwavesys.com',
    packages=packages,
    zip_safe=False,
)
