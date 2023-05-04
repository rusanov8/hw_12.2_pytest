import pytest

from utils import arrs


@pytest.fixture()
def arrs_fixture():
    return [1, 2, 3, 4]


def test_get(arrs_fixture):
    assert arrs.get(arrs_fixture, 1, "test") == 2
    assert arrs.get(arrs_fixture, -1, "test") == "test"
    with pytest.raises(IndexError):
        arrs.get([], 0, "test") == "test"
        arrs.get(arrs_fixture, 10, "test") == "test"


def test_slice(arrs_fixture):
    assert arrs.my_slice(arrs_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(arrs_fixture, 1) == [2, 3, 4]
    assert arrs.my_slice(arrs_fixture, -1, -2) == []
    assert arrs.my_slice(arrs_fixture, 10, 10) == []
    assert arrs.my_slice(arrs_fixture, 0) == [1, 2, 3, 4]
    assert arrs.my_slice(arrs_fixture, -5) == [1, 2, 3, 4]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([], -1, -2) == []
