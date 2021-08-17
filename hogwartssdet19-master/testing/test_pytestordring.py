"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 4:38 下午'
"""

import pytest


@pytest.mark.second
def test_foo():
    assert True


@pytest.mark.first
def test_bar():
    assert True


@pytest.mark.run(order=-1)
def test_bar2():
    assert True


@pytest.mark.run(order=-3)
def test_bar1():
    assert True
