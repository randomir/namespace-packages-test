import nox

@nox.session
@nox.parametrize('interpreter', ('python2', 'python3'))
def tests(session, interpreter):
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')
    session.install('native/a/', 'native/b/', 'native/b-c/')
    session.run('pytest')
