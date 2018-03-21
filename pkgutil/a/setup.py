from setuptools import setup

setup(
    name='root-a',
    version='0.1',
    description='Namespace package one level below root.',
    author='Radomir Stevanovic',
    author_email='radomir@dwavesys.com',
    packages=['root.a'],
    zip_safe=False,
)
