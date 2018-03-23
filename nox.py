import nox


@nox.session
@nox.parametrize('interpreter', ('python2', 'python3'))
def test_native__mixed_levels(session, interpreter):
    """`root.b` from `b` package overlaps with `root.b.c` from `b-c`. We're adding
    `root.a` here as a baseline case (it shouldn't overlap with `root.b`)."""
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')
    session.install('native/a/', 'native/b/', 'native/b-c/')
    session.run('pytest', 'tests/test_a.py', 'tests/test_b.py', 'tests/test_b-c.py')


@nox.session
@nox.parametrize('interpreter', ('python2', 'python3'))
def test_native__mixed_levels__mixed_module_def(session, interpreter):
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')
    session.install('native/b/', 'native/b-c/', 'native/b-de/')
    session.run('pytest', 'tests/test_b.py', 'tests/test_b-c.py', 'tests/test_b-de.py')


@nox.session
@nox.parametrize('interpreter', ('python2', 'python3'))
def test_pkgutil_mixed_levels(session, interpreter):
    """`root.b` from `b` package overlaps with `root.b.c` from `b-c`. We're adding
    `root.a` here as a baseline case (it shouldn't overlap with `root.b`)."""
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')
    session.install('pkgutil/a/', 'pkgutil/b/', 'pkgutil/b-c/')
    session.run('pytest', 'tests/test_a.py', 'tests/test_b.py', 'tests/test_b-c.py')


@nox.session
@nox.parametrize('interpreter', ('python2', 'python3'))
def test_pkgutil__mixed_levels__mixed_module_def(session, interpreter):
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')
    session.install('native/b/', 'native/b-c/', 'native/b-de/')
    session.run('pytest', 'tests/test_b.py', 'tests/test_b-c.py', 'tests/test_b-de.py')
