# Raw results

    $ nox
    ...snip...
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
