# Namespace packages: battle-testing

The goal of this repo is to test several hypotheses about namespace packages and
their usage in real-life scenarios. Tests are focused on Python 3, but for
completeness we run them in Python 2, too.

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

## Running tests

    $ pip install -r requirements.txt
    $ nox

## Preliminary results

    nox > * same_level_only(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python2'): success
    nox > * same_level_only(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): success
    nox > * same_level_only(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python2'): success
    nox > * same_level_only(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): success
    nox > * same_level_only(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python3'): success
    nox > * same_level_only(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): success
    nox > * same_level_only(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python3'): success
    nox > * same_level_only(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): success
    nox > * same_level_only(approach='native', install_command=('pip', 'install', '.'), interpreter='python2'): failed
    nox > * same_level_only(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): failed
    nox > * same_level_only(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python2'): failed
    nox > * same_level_only(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): failed
    nox > * same_level_only(approach='native', install_command=('pip', 'install', '.'), interpreter='python3'): success
    nox > * same_level_only(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): success
    nox > * same_level_only(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python3'): success
    nox > * same_level_only(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): success
    nox > * non_clashing_levels(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python2'): success
    nox > * non_clashing_levels(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): success
    nox > * non_clashing_levels(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python2'): success
    nox > * non_clashing_levels(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): success
    nox > * non_clashing_levels(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python3'): success
    nox > * non_clashing_levels(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): success
    nox > * non_clashing_levels(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python3'): success
    nox > * non_clashing_levels(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): success
    nox > * non_clashing_levels(approach='native', install_command=('pip', 'install', '.'), interpreter='python2'): failed
    nox > * non_clashing_levels(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): failed
    nox > * non_clashing_levels(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python2'): failed
    nox > * non_clashing_levels(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): failed
    nox > * non_clashing_levels(approach='native', install_command=('pip', 'install', '.'), interpreter='python3'): success
    nox > * non_clashing_levels(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): success
    nox > * non_clashing_levels(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python3'): success
    nox > * non_clashing_levels(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): success
    nox > * mixed_levels(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python2'): failed
    nox > * mixed_levels(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): failed
    nox > * mixed_levels(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python2'): failed
    nox > * mixed_levels(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): failed
    nox > * mixed_levels(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python3'): success
    nox > * mixed_levels(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): failed
    nox > * mixed_levels(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python3'): failed
    nox > * mixed_levels(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): failed
    nox > * mixed_levels(approach='native', install_command=('pip', 'install', '.'), interpreter='python2'): failed
    nox > * mixed_levels(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): failed
    nox > * mixed_levels(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python2'): failed
    nox > * mixed_levels(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): failed
    nox > * mixed_levels(approach='native', install_command=('pip', 'install', '.'), interpreter='python3'): success
    nox > * mixed_levels(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): failed
    nox > * mixed_levels(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python3'): failed
    nox > * mixed_levels(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): failed
    nox > * mixed_levels__mixed_module_def(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python2'): failed
    nox > * mixed_levels__mixed_module_def(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): failed
    nox > * mixed_levels__mixed_module_def(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python2'): failed
    nox > * mixed_levels__mixed_module_def(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): failed
    nox > * mixed_levels__mixed_module_def(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python3'): failed
    nox > * mixed_levels__mixed_module_def(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): failed
    nox > * mixed_levels__mixed_module_def(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python3'): failed
    nox > * mixed_levels__mixed_module_def(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): failed
    nox > * mixed_levels__mixed_module_def(approach='native', install_command=('pip', 'install', '.'), interpreter='python2'): failed
    nox > * mixed_levels__mixed_module_def(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): failed
    nox > * mixed_levels__mixed_module_def(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python2'): failed
    nox > * mixed_levels__mixed_module_def(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): failed
    nox > * mixed_levels__mixed_module_def(approach='native', install_command=('pip', 'install', '.'), interpreter='python3'): success
    nox > * mixed_levels__mixed_module_def(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): failed
    nox > * mixed_levels__mixed_module_def(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python3'): failed
    nox > * mixed_levels__mixed_module_def(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): failed
