"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/17 9:23 下午'
"""
import yaml


def test_demo():
    with open('datas.yml') as f:
        # safe_load 将文件流转成python 对象
        datas = yaml.safe_load(f)
    print(datas)