"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 3:57 下午'
"""
import pytest


@pytest.fixture()
def login():
    print("实现登录")
    # yield 相当于 return,
    # yield 前面的操作相当于setup
    # yield 后面的操作相当于teardown
    yield "username,nickname1111"
    print("登出")
