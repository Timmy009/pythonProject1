import pytest
from morning_code.tdd_first import no_ar


def test_add():
    assert no_ar(1000, 10) == 900


def test_negative():
    with pytest.raises(ValueError):
        no_ar(-9.99, 10)


def test_negative3():
    with pytest.raises(ValueError):
        no_ar(-9.99, 10)


def test_type():
    with pytest.raises(TypeError):
        no_ar("jfdhj", 10)
