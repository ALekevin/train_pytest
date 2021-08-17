## 霍格沃兹测试学院 测开19期

实战演练项目

## pytest 命名规则

- 文件名 test_开头或者 _test结尾
- 类名 Test开头
- 方法名 test_开头

## pytest 命令行参数

- pytest --help
- pytest -v 打印结果的详细信息
- pytest -s 打印print的信息
- pytest -vs -v -s 两个参数的简写

## pytest fixture

### pytest fixture 用法

1、使用 装饰器 来定义fixture @pyteset.fixture()
2、如果想引用fixture 的返回数据 的话，就使用fixture 的名字来引用。 3、如果不需要引用fixture的返回值，可以使用装饰器@pytest.mark.usefixtures('login') 来使用fixture

### pytest 重点

- 重点1: Pytest 常用参数
- 重点2: pytest 参数化与数据驱动
- 重点3: pytest fixture 的基本用法（autouse, conftest.py）
- 重点4: allure  (环境，feature,story, 日志 ，截图 ，视频)
- 重点5: 日志打印
- 了解： hook
