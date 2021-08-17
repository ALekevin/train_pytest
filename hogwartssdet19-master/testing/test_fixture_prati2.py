"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 4:05 下午'
"""
import allure
import pytest
import logging

'''
通过fixture获取测试数据
'''


@allure.feature("计算器")
class TestCalculator:
    @allure.title("相加功能_{get_datas[0]}_{get_datas[1]}")
    @allure.story("相加功能")
    def test_add(self, get_calc_object, get_datas):
        logging.info(f"test_add  数据 ：{get_datas}")
        assert get_datas[2] == get_calc_object.add(get_datas[0], get_datas[1])

    @pytest.mark.div
    def test_div(self, get_calc_object):
        # calc = Calculator()
        assert 1 == get_calc_object.div(1, 1)
