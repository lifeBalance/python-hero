from starter import hello_world


def test_greets(capsys):
    hello_world()
    assert capsys.readouterr().out == "Hello, world!\n"