"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 4:21 下午'
"""
import pytest


@pytest.fixture()
def get_ini(pytestconfig):
    marks = pytestconfig.getini('markers')
    log_cli = pytestconfig.getini('log_cli')
    print(marks, log_cli)


def test_pytestconfig(get_ini):
    pass
