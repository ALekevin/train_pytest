"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 3:50 下午'
"""
from typing import List

import pytest

# 登录步骤
import yaml

from pythoncode.calculator import Calculator


# conftest.py 文件是会预先被加载的
# 自定义的fixture
@pytest.fixture()
def login():
    print("实现登录")
    # yield 相当于 return,
    # yield 前面的操作相当于setup
    # yield 后面的操作相当于teardown
    yield "token=2432343214321grgragafadf"
    print("登出")


# 测试步骤 连接数据库
@pytest.fixture()
def connectDB():
    print('连接数据库')
    return 'database --- datas'


# 获取 计算器实例的fixture
@pytest.fixture(scope='class')
def get_calc_object():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")


# 获取 测试数据
def get_calc_data():
    with open('./datas/calc.yml') as f:
        totals = yaml.safe_load(f)
    return (totals['datas'], totals['ids'])


# request.param 实现了数据的获取
# ids 为每条数据起个别名，fixture实现
@pytest.fixture(params=get_calc_data()[0], ids=get_calc_data()[1])
def get_datas(request):
    return request.param


# 改写 pytest_collection_modifyitems hook 函数，
# 收集上来所有的测试用例之后，修改items的方法
# 一般hook 会放在conftest.py 文件中，
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print("items ===>", items)
    for item in items:
        # item.name 测试用例的名字
        # item.nodeid 测试用例的路径
        # print(item.name)
        # print(item.nodeid)
        # 修改测试用例的编码
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'hook' in item.name:
            item.add_marker(pytest.mark.hook)
        if 'aaa' in item.name:
            item.add_marker(pytest.mark.aaa)


# 添加一个命令行参数
def pytest_addoption(parser):
    # 添加一个组
    group = parser.getgroup("helloworld")
    # 添加一个命令行参数
    group.addoption(
        "--name",
        action="store",
        dest="name",
        default="World",
        help='Default "name" for hello().',
    )
