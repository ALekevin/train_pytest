"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 4:46 下午'
"""
from time import sleep

import pytest


@pytest.mark.second
def test_foo():
    sleep(1)
    assert True


@pytest.mark.first
def test_bar():
    sleep(1)
    assert True


@pytest.mark.run(order=-1)
def test_bar2():
    sleep(1)
    assert True


@pytest.mark.run(order=-3)
def test_bar1():
    sleep(1)
    assert True

# A B(A) C
