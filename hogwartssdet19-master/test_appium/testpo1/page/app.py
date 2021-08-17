"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/4 4:08 下午'
"""
# 启动， 关闭，重启app
from appium import webdriver

from test_appium.testpo1.page.main_page import MainPage


class App:
    def start(self):
        # 启动应用
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "hogwarts"
        caps["noReset"] = "true"
        # 提升 启动app速度的配置
        caps['skipDeviceInitialization'] = "true"
        # 只有 [动态页面] 才需要设置这个 时间
        # caps["settings[waitForIdleTimeout]"] = 0
        # 至关重要的一行  与appium 服务建立连接，并传递一个caps 字典对象
        # 第一次与server 建立 连接，会创建一个 session sessionid
        self.driver = webdriver.Remote("http://127.0.0.1:4725/wd/hub", caps)
        # 隐式等待 5s 动态的等待元素出现，如果五秒 之内都没有找到元素，就会抛异常
        # 隐式等待什么时候被调用的？每次调用find_element/s 方法的时候都会动态的等待
        self.driver.implicitly_wait(5)
        return self

    def restart(self):
        pass

    def quit(self):
        pass

    def goto_main(self):
        # 进入主页 入口
        return MainPage(self.driver)
