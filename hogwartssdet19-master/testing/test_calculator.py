"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/17 8:28 下午'
"""
import logging

import pytest
import yaml

from pythoncode.calculator import Calculator

# 获取 测试数据
def get_calc_data():
    with open('./datas/calc.yml') as f:
        totals = yaml.safe_load(f)
    return (totals['datas'],totals['ids'])

# 测试 获取数据的方法
def test_getdatas():
    print(get_calc_data())


class TestCalculator:
    # setup teardown 每条用例前后分别被调用
    # setup_class teardown_class 在类执行的前后分别被调用一次
    def setup_class(self):
        print("开始计算")
        logging.info("开始计算")
        # 加了self 之后，calc就变成了实例变量，就可以在其它的用例当中调用了
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect',get_calc_data()[0],ids=get_calc_data()[1])
    def test_add(self,a,b,expect):
        # calc = Calculator()
        assert expect == self.calc.add(a, b)

    # @pytest.mark.add
    # def test_add1(self):
    #     # calc = Calculator()
    #     assert 2000 == self.calc.add(1000, 1000)

    @pytest.mark.div
    def test_div(self):
        # calc = Calculator()
        assert 1 == self.calc.div(1, 1)
