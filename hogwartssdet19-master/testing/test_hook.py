"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 4:58 下午'
"""
import pytest


@pytest.mark.parametrize('name', ['赫敏', ' 哈利波特'], ids=['赫敏', ' 哈利波特'])
def test_hook(name):
    print(f"姓名 ： {name}")


def test_aaa():
    print("testaaaa")
