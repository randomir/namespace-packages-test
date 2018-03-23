import nox

def prepend_to_all(prefix, items):
    return [prefix + item for item in items]


@nox.session
@nox.parametrize('approach', ('pkgutil', 'native'))
@nox.parametrize('interpreter', ('python2', 'python3'))
def same_level_only(session, approach, interpreter):
    """Base case: `root.a` and `root.b`."""
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')
    session.install(*prepend_to_all(approach, ['/a/', '/b/']))
    session.run('pytest', 'tests/test_a.py', 'tests/test_b.py')


@nox.session
@nox.parametrize('approach', ('pkgutil', 'native'))
@nox.parametrize('interpreter', ('python2', 'python3'))
def non_clashing_levels(session, approach, interpreter):
    """Base case: `root.a` and `root.b.c`."""
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')
    session.install(*prepend_to_all(approach, ['/a/', '/b-c/']))
    session.run('pytest', 'tests/test_a.py', 'tests/test_b-c.py')


@nox.session
@nox.parametrize('approach', ('pkgutil', 'native'))
@nox.parametrize('interpreter', ('python2', 'python3'))
def mixed_levels(session, approach, interpreter):
    """`root` in `b` is a clean namespace package, but `root.b` is not (`b` is
    not a 'stem', but a 'leaf'). I.e., `root.b` from `b` package overlaps with
    `root.b.c` from `b-c`.

    We're adding `root.a` here as a baseline case (it shouldn't overlap with
    `root.b`).
    """
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')
    session.install(*prepend_to_all(approach, ['/a/', '/b/', '/b-c/']))
    session.run('pytest', 'tests/test_a.py', 'tests/test_b.py', 'tests/test_b-c.py')


@nox.session
@nox.parametrize('approach', ('pkgutil', 'native'))
@nox.parametrize('interpreter', ('python2', 'python3'))
def mixed_levels__mixed_module_def(session, approach, interpreter):
    """Like `mixed_levels`, but with additional package that mixes module
    definition types: `b-de` package defined `root.b.d` with file (``root/b/d.py``),
    and `root.b.e` with dir/init (``root/b/e/__init__.py``).
    """
    session.interpreter = interpreter
    session.install('-r', 'tests/requirements.txt')
    session.install(*prepend_to_all(approach, ['/b/', '/b-c/', '/b-de/']))
    session.run('pytest', 'tests/test_b.py', 'tests/test_b-c.py', 'tests/test_b-de.py')
