from starter import contains_duplicate


def test_has_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) is True


def test_all_distinct():
    assert contains_duplicate([1, 2, 3, 4]) is False


def test_many_duplicates():
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2]) is True


def test_single_element():
    assert contains_duplicate([7]) is False
