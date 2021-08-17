"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 4:09 下午'
"""
import pytest

'''
fixture实现参数化
类似于参数化的功能，也可以通过ids 为测试用例起别名
'''


# request 是 pytest 内置的fixture,
# 可以拿过来直接使用，通过request.param 来获取 参数列表
@pytest.fixture(params=['tom', 'jerry', 'linda'], ids=['name1', 'name2', 'name3'])
def login(request):
    myparam = request.param
    print(f"用户名：{myparam}")
    yield myparam
    print("登录操作")


def test_case1(login):
    print(login)
