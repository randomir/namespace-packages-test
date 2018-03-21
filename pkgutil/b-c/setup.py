from setuptools import setup

setup(
    name='root-b-c',
    version='0.1',
    description='Namespace package two levels below root.',
    author='Radomir Stevanovic',
    author_email='radomir@dwavesys.com',
    packages=['root.b.c'],
    zip_safe=False,
)
