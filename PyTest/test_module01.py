import pytest
pytestmark = [pytest.mark.smoke]
def test_a5():
    assert 5+5 ==10
    assert 5-5 ==0
    assert 5*5 ==25

def test_a6():
    assert 10/2 ==5, "The test is failed"

def test_a7():
    assert 10//4 ==2
