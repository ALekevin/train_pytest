"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 2:24 下午'
"""
# 数据驱动 yaml
# pip install pyyaml
# 使用导入 yaml
import yaml


# yaml.safe_load()  将文件流转成 python 对象
# yaml.safe_dump()  将python 对象转成yaml格式

def get_calcdatas():
    with open('./datas/calc_homework.yml') as f:
        data = yaml.safe_load(f)
    print(data)
    # return None
    return data


def test_get_calcdata():
    datas = get_calcdatas()['add']['int']['datas']
    ids = get_calcdatas()['add']['int']['ids']
    print(datas, ids)


def test_yamldump():
    datas = {'add': {'int': {'datas': [[1, 1, 2], [100, 100, 200], [0, 1, 1]], 'ids': ['int', 'bigint', 'zero']},
                     'float': {'datas': [[0.1, 0.1, 0.2], [0.1, 0.2, 0.3]], 'ids': ['float1', 'float2']}}}
    with open('./datas/meta.yml', mode='w', encoding='utf-8') as f:
        # python 对象 转成 yaml 数据
        yaml.safe_dump(datas, f)
