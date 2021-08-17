"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 3:07 下午'
"""
'''
作用域
'''
import pytest


@pytest.fixture(scope='module', autouse=True)
def login():
    print("login")
    return "token"


def test_case1():
    print("case1")


def test_case2():
    print("case2")


def test_case3():
    print("case3")
