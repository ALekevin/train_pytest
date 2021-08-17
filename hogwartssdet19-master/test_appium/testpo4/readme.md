## 第三次优化 ： 日志

### 并发执行

一个appium server 可以测试一台设备 多个appium server 测试多台测试

### 启动appium server

通过指定不同的端口，来启动不同的服务

appium --session-override -p 4723 appium --session-override -p 4725

### 代码端

- 指定udid（运行不同的设备需要）
- 端口port

### 运行

mac： udid='192.168.57.103:5555' port='4723' pytest test_addcontact.py udid='emulator-5554' port='4725' pytest
test_addcontact.py

windows:
set udid='192.168.57.103:5555' set port='4723'
pytest test_addcontact.py

多台设备 需要写个shell脚本 ，多进程的方式启动起来。