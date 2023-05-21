import pytest
from morning_code.Zeroed import zero_re

def test_return_answer():
    lst = ["str", 5, "goat", 6, 7, 8]
    assert zero_re(lst) == [0, 5, "goat", 6, 7, 0]



