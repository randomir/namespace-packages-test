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

## Raw results

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
    nox > * uninstall__same_level_only(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python2'): failed
    nox > * uninstall__same_level_only(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): success
    nox > * uninstall__same_level_only(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python2'): success
    nox > * uninstall__same_level_only(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): success
    nox > * uninstall__same_level_only(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python3'): success
    nox > * uninstall__same_level_only(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): success
    nox > * uninstall__same_level_only(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python3'): success
    nox > * uninstall__same_level_only(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): success
    nox > * uninstall__same_level_only(approach='native', install_command=('pip', 'install', '.'), interpreter='python2'): failed
    nox > * uninstall__same_level_only(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): failed
    nox > * uninstall__same_level_only(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python2'): failed
    nox > * uninstall__same_level_only(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): failed
    nox > * uninstall__same_level_only(approach='native', install_command=('pip', 'install', '.'), interpreter='python3'): success
    nox > * uninstall__same_level_only(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): success
    nox > * uninstall__same_level_only(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python3'): success
    nox > * uninstall__same_level_only(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): success
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
    nox > * uninstall__non_clashing_levels(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python2'): failed
    nox > * uninstall__non_clashing_levels(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): success
    nox > * uninstall__non_clashing_levels(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python2'): success
    nox > * uninstall__non_clashing_levels(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): success
    nox > * uninstall__non_clashing_levels(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python3'): success
    nox > * uninstall__non_clashing_levels(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): success
    nox > * uninstall__non_clashing_levels(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python3'): success
    nox > * uninstall__non_clashing_levels(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): success
    nox > * uninstall__non_clashing_levels(approach='native', install_command=('pip', 'install', '.'), interpreter='python2'): failed
    nox > * uninstall__non_clashing_levels(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): failed
    nox > * uninstall__non_clashing_levels(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python2'): failed
    nox > * uninstall__non_clashing_levels(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): failed
    nox > * uninstall__non_clashing_levels(approach='native', install_command=('pip', 'install', '.'), interpreter='python3'): success
    nox > * uninstall__non_clashing_levels(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): success
    nox > * uninstall__non_clashing_levels(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python3'): success
    nox > * uninstall__non_clashing_levels(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): success
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
    nox > * uninstall__mixed_levels(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python2'): failed
    nox > * uninstall__mixed_levels(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): success
    nox > * uninstall__mixed_levels(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python2'): success
    nox > * uninstall__mixed_levels(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): success
    nox > * uninstall__mixed_levels(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python3'): success
    nox > * uninstall__mixed_levels(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): success
    nox > * uninstall__mixed_levels(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python3'): success
    nox > * uninstall__mixed_levels(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): success
    nox > * uninstall__mixed_levels(approach='native', install_command=('pip', 'install', '.'), interpreter='python2'): failed
    nox > * uninstall__mixed_levels(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): failed
    nox > * uninstall__mixed_levels(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python2'): failed
    nox > * uninstall__mixed_levels(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): failed
    nox > * uninstall__mixed_levels(approach='native', install_command=('pip', 'install', '.'), interpreter='python3'): success
    nox > * uninstall__mixed_levels(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): success
    nox > * uninstall__mixed_levels(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python3'): success
    nox > * uninstall__mixed_levels(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): success
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
    nox > * uninstall__mixed_levels__mixed_module_def(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python2'): failed
    nox > * uninstall__mixed_levels__mixed_module_def(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): failed
    nox > * uninstall__mixed_levels__mixed_module_def(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python2'): failed
    nox > * uninstall__mixed_levels__mixed_module_def(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): failed
    nox > * uninstall__mixed_levels__mixed_module_def(approach='pkgutil', install_command=('pip', 'install', '.'), interpreter='python3'): failed
    nox > * uninstall__mixed_levels__mixed_module_def(approach='pkgutil', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): failed
    nox > * uninstall__mixed_levels__mixed_module_def(approach='pkgutil', install_command=('python', 'setup.py', 'install'), interpreter='python3'): failed
    nox > * uninstall__mixed_levels__mixed_module_def(approach='pkgutil', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): failed
    nox > * uninstall__mixed_levels__mixed_module_def(approach='native', install_command=('pip', 'install', '.'), interpreter='python2'): failed
    nox > * uninstall__mixed_levels__mixed_module_def(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python2'): failed
    nox > * uninstall__mixed_levels__mixed_module_def(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python2'): failed
    nox > * uninstall__mixed_levels__mixed_module_def(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python2'): failed
    nox > * uninstall__mixed_levels__mixed_module_def(approach='native', install_command=('pip', 'install', '.'), interpreter='python3'): success
    nox > * uninstall__mixed_levels__mixed_module_def(approach='native', install_command=('pip', 'install', '-e', '.'), interpreter='python3'): failed
    nox > * uninstall__mixed_levels__mixed_module_def(approach='native', install_command=('python', 'setup.py', 'install'), interpreter='python3'): failed
    nox > * uninstall__mixed_levels__mixed_module_def(approach='native', install_command=('python', 'setup.py', 'develop'), interpreter='python3'): failed

## Interpreted results

### Basic case, vanilla namespace packages (`same_level_only` and `non_clashing_levels`)

  - `root` is an empty shared namespace for `root.a` and `root.b` (split in two packages),
    or for `root.a` and `root.b.c`
  - `pkgutil` approach works for all install type variants, in all Python versions
  - development and regular install work equally well
  - in Python 2, for regular pip install method, uninstall of one package breaks the import of the other
  - (fully) works in Python 3 (all test cases pass)
  - developer install works in Python 2, but regular uninstall doesn't

### Partially overlapping namespaces (`mixed_levels`)

  - `root.b` is not empty, yet we try to overlap it with `root.b.c`
  - (fully) works only in Python 3 for only regular pip installs, but both approaches

### Overlapping namespaces, with mixed module definitions (`mixed_levels__mixed_module_def`)

  - non-empty `root.b` is overlapped with `root.b.c` (as in previous case), but then also
    with `root.b.d` (implemented in module file `d.py`) and `root.b.e` (implemented in `e/__init__.py`)
  - (fully) works only in Python 3 for only regular pip installs and only `native` approach

## Conclusions

  - For full Python 2 and 3 compatibility, all stem `__init__.py` must be empty.

  - Developer installs work.

  - Uninstall works in Python 3 and mostly in Python 2.

  - To have autocomplete on second-level packages, clashing namespaces would have to be used,
    and those work only for native namespace packages in Python 3.
