"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 4:05 下午'
"""
import logging
import pytest
import yaml


# 获取 测试数据
def get_calc_data():
    with open('./datas/calc.yml') as f:
        totals = yaml.safe_load(f)
    return (totals['datas'], totals['ids'])


# 测试 获取数据的方法
def test_getdatas():
    print(get_calc_data())


class TestCalculator:
    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect', get_calc_data()[0], ids=get_calc_data()[1])
    def test_add(self, get_calc_object, a, b, expect):
        assert expect == get_calc_object.add(a, b)

    @pytest.mark.div
    def test_div(self, get_calc_object):
        # calc = Calculator()
        assert 1 == get_calc_object.div(1, 1)
