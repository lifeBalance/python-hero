from starter import running_sum


def test_example():
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]


def test_all_ones():
    assert running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]


def test_mixed():
    assert running_sum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]


def test_negatives():
    assert running_sum([-1, 1, -1, 1]) == [-1, 0, -1, 0]
