from problem import quiz


def check(want, *args):
    assert quiz(*args) == want, f"quiz{args} should be {want}"


# Write this exercise's tests.
def test_it():
    check(None)
