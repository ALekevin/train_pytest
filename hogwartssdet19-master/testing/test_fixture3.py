"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 2:58 下午'
"""
import pytest


# autouse=True 自动应用,默认是false

@pytest.fixture()
def login():
    print("login")
    return "token"


def test_case1():
    print("case1")


def test_case2():
    print("case2")


def test_case3():
    print("case3")
