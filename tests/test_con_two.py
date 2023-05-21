import pytest
from morning_code.Take_in import ret

def test_add():
    assert ret(2.3, 5.5) == 7.8


def test_con():
    with pytest.raises(TypeError):
        ret(2, 4)