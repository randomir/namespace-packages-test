The goal of this repo is to test several hypothesis about namespace packages in
Python 2, and more importantly in Python 3.

Different approaches for creating namespace packages are covered in PyPA's
[Packaging namespace packages](https://packaging.python.org/guides/packaging-namespace-packages/)
document, as well in [PEP-420](https://www.python.org/dev/peps/pep-0420).
Basic examples are given in [pypa/sample-namespace-packages](https://github.com/pypa/sample-namespace-packages)
GitHub repository.

Here we're extending these samples (for `native` and `pkgutil` approaches) to
test the following claims:

 - no autocomplete on second-level packages
 - all stem `__init__.py` must be empty
 - uninstalls break the namespace
 - developer installs might not work effectively
