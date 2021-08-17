"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 3:50 下午'
"""
'''
理解 conftest11.py
在当前目录下创建一个conftest.py文件
1、conftest.py 文件不需要导入，直接引用 里面定义的fixture方法
2、就近原则， 当前模块> 当前目录的conftest.py > 父级目录的conftest.py>祖辈目录（不会找兄弟给过点）
3、一点来说，conftest.py会存放一些公共的方法，比如fixture, 还有hook 
'''


def test_case1(login, connectDB):
    pass
    # print(login)
    # print("case1")


def test_case2(login):
    pass
    # print("case2")


def test_case3(login):
    pass
    # print("case3")
