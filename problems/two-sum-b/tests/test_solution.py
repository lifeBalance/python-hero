from starter import two_sum


def check(want, *args):
    # Sorted, because the exercise lets you return the indices in either order.
    assert sorted(two_sum(*args)) == want, f"two_sum{args} should be {want}"


def test_example():
    check([0, 1], [2, 7, 11, 15], 9)


def test_pair_not_at_start():
    check([1, 2], [3, 2, 4], 6)


def test_same_value_twice():
    check([0, 1], [3, 3], 6)


def test_negative_numbers():
    check([2, 4], [-1, -2, -3, -4, -5], -8)