from problem import bar


def check(want, *args):
    assert bar(*args) == want, f"bar{args} should be {want}"


# Write this exercise's tests.
def test_it():
    check(None)
