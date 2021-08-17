## 第二步封装：基类

base_page.py 主要用来存放最基本的方法 比如：实例 driver ,查找 find ,find_and_click, find_and_sendkeys

- 第一步：优化所有的页面 去掉__init__()方法
- 第二步：优化所有页面的 find ,find_and_click, find_and_sendkeys, 或者其它的常用的基本方法，滑动查找，获取toast