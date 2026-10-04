from problem import foo


def check(want, *args):
    assert foo(*args) == want, f"foo{args} should be {want}"


# Write this exercise's tests.
def test_it():
    check(None)
