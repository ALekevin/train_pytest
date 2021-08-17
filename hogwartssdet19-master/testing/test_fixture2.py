"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 2:55 下午'
"""
import pytest

'''
fixture 与参数同时存在的情况 
'''


#
@pytest.fixture()
def login():
    print("login")
    return "token"


@pytest.mark.parametrize('a,b', [[1, 2], [3, 4]])
def test_param(login, a, b):
    print(a, b, login)
