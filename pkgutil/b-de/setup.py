import sys
from setuptools import setup

packages = ['root.b', 'root.b.e']

if sys.version_info.major == 2:
    packages += ['root']

setup(
    name='root-b-de',
    version='0.1',
    description='Namespace package two levels below root.',
    author='Radomir Stevanovic',
    author_email='radomir@dwavesys.com',
    packages=packages,
    zip_safe=False,
)
