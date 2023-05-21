import pytest
from morning_code.Name import gmail

def test_return_answer():
    assert gmail("timmy") == "timmy@gmail.com"

def test_int():
    with pytest.raises(TypeError):
        gmail(78)



