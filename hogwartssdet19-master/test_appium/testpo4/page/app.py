"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/4 4:08 下午'
"""
# 启动， 关闭，重启app
import os

from appium import webdriver

from test_appium.testpo4.page.base_page import BasePage
from test_appium.testpo4.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            # 启动应用
            print("driver == None 创建driver")
            udid = os.getenv('udid')
            port = os.getenv('port')
            caps = {}
            caps["platformName"] = "Android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["deviceName"] = "hogwarts"
            caps["noReset"] = "true"
            caps['udid'] = udid
            # 提升 启动app速度的配置
            caps['skipDeviceInitialization'] = "true"
            # 只有 [动态页面] 才需要设置这个 时间
            # caps["settings[waitForIdleTimeout]"] = 0
            # 至关重要的一行  与appium 服务建立连接，并传递一个caps 字典对象
            # 第一次与server 建立 连接，会创建一个 session sessionid
            self.driver = webdriver.Remote(f"http://127.0.0.1:{port}/wd/hub", caps)
            # 隐式等待 5s 动态的等待元素出现，如果五秒 之内都没有找到元素，就会抛异常
            # 隐式等待什么时候被调用的？每次调用find_element/s 方法的时候都会动态的等待
            self.driver.implicitly_wait(5)
        else:
            print('driver != None 复用driver')
            # launch_app() 帮我启动应用
            # start_activity 可以启动任何应用
            # self.driver.start_activity()
            self.driver.launch_app()

        return self

    def restart(self):
        self.driver.close()
        self.driver.launch_app()

    def quit(self):
        self.driver.quit()

    def goto_main(self):
        # 进入主页 入口
        return MainPage(self.driver)
