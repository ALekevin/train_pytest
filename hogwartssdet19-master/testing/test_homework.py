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
    with open('./datas/calc_homework.yml') as f:
        totals = yaml.safe_load(f)
    # return (totals['datas'],totals['ids'])
    # return totals
    add_int_datas = totals['add']['int']['datas']
    add_int_ids = totals['add']['int']['ids']
    return (add_int_datas, add_int_ids)


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

    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0.1, 0.2], [0.1, 0.2, 0.3]
    ])
    def test_add_float(self, a, b, expect):
        assert expect == round((a + b), 2)

    @pytest.mark.div
    def test_div_zero(self):
        # calc = Calculator()
        # assert 1 == self.calc.div(1, 0)
        # 捕获 ZeroDivisionError 异常，处理为正常的执行结果
        with pytest.raises(ZeroDivisionError):
            assert 'afdfaasf' == self.calc.div(1, 0)

    @pytest.mark.div
    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0.1, 0.2], [0.1, 0.2, 0.3]
    ])
    def test_div_float(self, a, b, expect):
        assert expect == a / b
