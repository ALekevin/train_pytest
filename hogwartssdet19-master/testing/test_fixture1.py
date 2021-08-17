"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 2:44 下午'
"""
# fixture 基本用法1

# 测试步骤 登录
import pytest


# 测试步骤的方法上面加上装饰器@pytest.fixture()，这个测试步骤 就变成了pytest fixture
@pytest.fixture()
def login():
    print("login")
    return "token"


# 测试步骤 连接数据库
@pytest.fixture()
def connectDB():
    print('连接数据库')
    return 'database --- datas'


def test_case1(login, connectDB):
    print(f"登录操作的返回数据 ：{login}")
    print(f"连接数据库的返回数据 ：{connectDB} ")
    # 登录
    # login()
    # 连接数据库
    # connectDB()
    print("case1")


# 使用装饰器的方式引用fixture
@pytest.mark.usefixtures('login')
def test_case2():
    print("case2")


def test_case3(login):
    # 登录
    # login()
    print("case3")
