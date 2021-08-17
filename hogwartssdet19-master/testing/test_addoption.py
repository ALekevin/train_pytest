"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 5:21 下午'
"""


def test_a(pytestconfig):
    result = pytestconfig.getoption('--name')
    print(result)
