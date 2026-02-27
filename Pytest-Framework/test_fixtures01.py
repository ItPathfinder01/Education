import pytest

@pytest.fixture()
def setup_list():
    print("\n in fixtures... \n")
    city = ["New York", "Minsk", "Tel Aviv", "Motreal", "Tbilisi"]
    return city

def test_getItem(setup_list):
    assert setup_list[0] == "New York"
    assert setup_list[::2] == ["New York", "Tel Aviv", "Tbilisi"]

def test_reverseList(setup_list):
    assert setup_list[::-2] == ["Tbilisi", "Tel Aviv", "New York"]

