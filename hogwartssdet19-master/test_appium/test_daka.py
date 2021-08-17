"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/1 9:00 下午'
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWeXin:
    def setup(self):
        # 资源准备  打开应用
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "hogwarts"
        caps["noReset"] = "true"
        # 提升 启动app速度的配置
        caps['skipDeviceInitialization'] = "true"
        # 只有 [动态页面] 才需要设置这个 时间
        caps["settings[waitForIdleTimeout]"] = 0
        # 至关重要的一行  与appium 服务建立连接，并传递一个caps 字典对象
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 隐式等待 5s 动态的等待元素出现，如果五秒 之内都没有找到元素，就会抛异常
        # 每次调用find_element/s 方法的时候都会动态的等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 资源的回收
        self.driver.quit()

    def test_daka(self):
        '''
        前提条件
        已登录状态（ noReset=True）
        打卡用例：
        1、打开【企业微信】应用
        2、进入【工作台】
        3、点击【打卡】
        4、选择【外出打卡】tab
        5、点击【第N次打卡】
        6、验证【外出打卡成功】
        7、退出【企业微信】应用
        :return:
        '''
        # 知识点1: Mobile_by 继承 by ，拥有了by 所有的属性又添加了移动端的支持
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 与下面的写法是一个意思
        # self.driver.find_element_by_xpath()
        # 如果要是要找的元素没有展示在当前页面， 要滑动查找这个元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).\
                                 instance(0)).scrollIntoView(new UiSelector().\
                                 text("打卡").instance(0));').click()
        # sleep(1)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")
        # WebDriverWait(self.driver,10).until(lambda x:x.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']"))
