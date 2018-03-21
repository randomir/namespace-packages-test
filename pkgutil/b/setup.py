from setuptools import setup

setup(
    name='root-b',
    version='0.1',
    description='Namespace package one level below root.',
    author='Radomir Stevanovic',
    author_email='radomir@dwavesys.com',
    packages=['root.b'],
    zip_safe=False,
)
