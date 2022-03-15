import pytest


# TODO: Comment the line bellow to see the test fail
@pytest.mark.xfail()
def test_assert_does_nice_things():
    assert [1, 2] == [1, 3]


# TODO: Comment the line bellow to see the test fail
@pytest.mark.xfail()
def test_assert_does_nice_things_nested():
    expected = {"thing": 3, "list": [1, 2]}
    actual = {"thing": 3, "list": [1, "banana"]}
    assert expected == actual
