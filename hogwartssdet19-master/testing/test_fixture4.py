"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 3:03 下午'
"""

'''
fixture 可以引用其它的fixture
'''
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]
