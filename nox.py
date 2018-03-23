import os
import nox


basedir = os.path.abspath(os.path.dirname(__file__))

install_commands = (
    ('pip', 'install', '.'),
    ('pip', 'install', '-e', '.'),
    ('python', 'setup.py', 'install'),
    ('python', 'setup.py', 'develop'))


def prepend_to_all(prefix, items):
    return [prefix + item for item in items]


def install_packages(session, package_paths, install_command):
    """Install all packages given in `package_paths` in `session`, using
    `install_command`.
    """
    for package_path in package_paths:
        session.chdir(package_path)
        session.run('rm', '-rf', 'dist', 'build', '*.egg-info')
        session.run(*install_command)
        session.chdir(basedir)


def init_session(session, interpreter):
    """Common `session` init for all tests."""
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')


@nox.session
@nox.parametrize('approach', ('pkgutil', 'native'))
@nox.parametrize('interpreter', ('python2', 'python3'))
@nox.parametrize('install_command', install_commands)
def same_level_only(session, approach, interpreter, install_command):
    """Base case: `root.a` and `root.b`."""
    init_session(session, interpreter)
    install_packages(session, prepend_to_all(approach, ['/a/', '/b/']), install_command)
    session.run('pytest', 'tests/test_a.py', 'tests/test_b.py')


@nox.session
@nox.parametrize('approach', ('pkgutil', 'native'))
@nox.parametrize('interpreter', ('python2', 'python3'))
@nox.parametrize('install_command', install_commands)
def non_clashing_levels(session, approach, interpreter, install_command):
    """Base case: `root.a` and `root.b.c`."""
    init_session(session, interpreter)
    install_packages(session, prepend_to_all(approach, ['/a/', '/b-c/']), install_command)
    session.run('pytest', 'tests/test_a.py', 'tests/test_b-c.py')


@nox.session
@nox.parametrize('approach', ('pkgutil', 'native'))
@nox.parametrize('interpreter', ('python2', 'python3'))
@nox.parametrize('install_command', install_commands)
def mixed_levels(session, approach, interpreter, install_command):
    """`root` in `b` is a clean namespace package, but `root.b` is not (`b` is
    not a 'stem', but a 'leaf'). I.e., `root.b` from `b` package overlaps with
    `root.b.c` from `b-c`.

    We're adding `root.a` here as a baseline case (it shouldn't overlap with
    `root.b`).
    """
    init_session(session, interpreter)
    install_packages(session, prepend_to_all(approach, ['/a/', '/b/', '/b-c/']), install_command)
    session.run('pytest', 'tests/test_a.py', 'tests/test_b.py', 'tests/test_b-c.py')


@nox.session
@nox.parametrize('approach', ('pkgutil', 'native'))
@nox.parametrize('interpreter', ('python2', 'python3'))
@nox.parametrize('install_command', install_commands)
def mixed_levels__mixed_module_def(session, approach, interpreter, install_command):
    """Like `mixed_levels`, but with additional package that mixes module
    definition types: `b-de` package defined `root.b.d` with file (``root/b/d.py``),
    and `root.b.e` with dir/init (``root/b/e/__init__.py``).
    """
    init_session(session, interpreter)
    install_packages(session, prepend_to_all(approach, ['/b/', '/b-c/', '/b-de/']), install_command)
    session.run('pytest', 'tests/test_b.py', 'tests/test_b-c.py', 'tests/test_b-de.py')
