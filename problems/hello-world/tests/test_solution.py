from starter import hello_world


def check(capsys, want, *args):
    hello_world(*args)
    assert capsys.readouterr().out == want, f"hello_world{args} should print {want!r}"


def test_greets(capsys):
    check(capsys, "Hello, world!\n")


def test_greets_somebody(capsys):
    check(capsys, "Hello, mankee!\n", "mankee")