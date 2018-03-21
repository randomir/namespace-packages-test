import nox


@nox.session
@nox.parametrize('interpreter', ('python2', 'python3'))
def test_native(session, interpreter):
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')
    session.install('native/a/', 'native/b/', 'native/b-c/')
    session.run('pytest')


@nox.session
@nox.parametrize('interpreter', ('python2', 'python3'))
def test_pkgutil_mixed_levels(session, interpreter):
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')
    session.install('pkgutil/a/', 'pkgutil/b/', 'pkgutil/b-c/')
    session.run('pytest')


@nox.session
@nox.parametrize('interpreter', ('python2', 'python3'))
def test_pkgutil_same_level_only(session, interpreter):
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')
    session.install('pkgutil/a/', 'pkgutil/b/')
    session.run('pytest', 'tests/test_a.py', 'tests/test_b.py')


@nox.session
@nox.parametrize('interpreter', ('python2', 'python3'))
def test_pkgutil_non_clashing_levels(session, interpreter):
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')
    session.install('pkgutil/a/', 'pkgutil/b-c/')
    session.run('pytest', 'tests/test_a.py', 'tests/test_c.py')
