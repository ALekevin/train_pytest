"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 3:11 下午'
"""

import pytest

'''
yield 激活teardown操作
python 的一个关键字
'''
'''
1、如果不加autouse=True，需要在用到fixture的地方，将这个fixture的名字传递到用例中
2、如果在测试用例中需要用到fixture的返回数据 ，那么一定要在用例的参数中，加上这个fixture的名字  
'''
'''
通过命令行参数 --setup-show 分析fixture 的执行过程，
每个fixture 其实都会默认执行两次，使用了yield之后，会激活第二次执行的操作，也就是
teardown操作内容。
pytest test_fixture6.py --setup-show

'''


@pytest.fixture()
def login():
    print("实现登录")
    # yield 相当于 return,
    # yield 前面的操作相当于setup
    # yield 后面的操作相当于teardown
    yield "token=2432343214321grgragafadf"
    print("登出")


def test_case1(login):
    pass
    # print(login)
    # print("case1")


def test_case2(login):
    pass
    # print("case2")


def test_case3(login):
    pass
    # print("case3")
