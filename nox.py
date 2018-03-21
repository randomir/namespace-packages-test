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
def test_pkgutil(session, interpreter):
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')
    session.install('pkgutil/a/', 'pkgutil/b/', 'pkgutil/b-c/')
    session.run('pytest')
