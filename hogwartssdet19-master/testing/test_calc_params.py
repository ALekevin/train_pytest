"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/17 8:12 下午'
"""
# 被测方法
import pytest


def add(a, b):
    return a + b


'''
相加功能的测试用例：
1、整数
2、小数的情况
3、为0的情况
4、大数
5、负数
'''


# 测试方法
# 将变化的数据提取出来 ，作为参数传递进去，
# a,b,expect 名字随便起，但是用例的参数要与 装饰器中的第一个参数一致
# 测试数据，
@pytest.mark.parametrize('a,b,expect', [
    [1, 1, 2], [100, 200, 300]
])
def test_add1(a, b, expect):
    assert expect == add(a, b)


def test_add2():
    assert 300 == add(100, 200)


def test_add3():
    assert 200 == add(0, 200)


def test_add4():
    assert 100 == add(-100, 200)


def test_add5():
    assert 0.2 == add(0.1, 0.1)


@pytest.mark.parametrize('a,b', [[1, 1], [1, 2], [2, 2]], ids=['int1', 'int2', 'int3'])
def test_add(a, b):
    print(a, b)


# a : 1,2,3
# b:  4,5,6
@pytest.mark.parametrize('b',[4,5,6,7,7])
@pytest.mark.parametrize('a',[1,2,3])
def test_demo(a, b):
    print(a,b)

