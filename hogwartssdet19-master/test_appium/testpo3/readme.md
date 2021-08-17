## 第三次封装：driver 利用

在app.py 里判断 driver 是否为 None,

- 如果为None 创建一个新的driver
- 如果不为None 则复用这个driver

## 启动app

- launch_app()  启动应用，caps里设置的activity
- start_activity(package,activity) 可以启动任何应用