"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/20 3:40 下午'
"""
'''
yield 用法
python 里可以实现生成器
'''


# 生成器
def provider():
    for i in range(1, 1000):
        print("start")
        yield i  # 相当于return，返回数据，如果不加i，也可以不返回数据
        # 记录上一次的执行位置，下一次继续执行后面的内容。
        print("end")


p = provider()
print(next(p))  # 1
print(next(p))  # 2
print(next(p))  # 3

# for x in p:
#     print(x)
