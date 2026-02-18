import pytest

@pytest.mark.parametrize("test_input", [45,55,65,75])
def test_param01(test_input):
    assert test_input < 75

