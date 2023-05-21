from OOP.Multiply import add_up


def test_add():
    assert add_up(5, 6) == 11
    result = add_up("David", " Esther") == "David Esther"
    assert type(result) == bool
