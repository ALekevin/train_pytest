"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/1 9:00 下午'
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from faker import Faker


class TestWeXin:
    def setup_class(self):
        self.fake = Faker('zh_CN')

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
        # caps["settings[waitForIdleTimeout]"] = 0
        # 至关重要的一行  与appium 服务建立连接，并传递一个caps 字典对象
        # 第一次与server 建立 连接，会创建一个 session sessionid
        self.driver = webdriver.Remote("http://127.0.0.1:4725/wd/hub", caps)
        # 隐式等待 5s 动态的等待元素出现，如果五秒 之内都没有找到元素，就会抛异常
        # 隐式等待什么时候被调用的？每次调用find_element/s 方法的时候都会动态的等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 资源的回收
        self.driver.quit()

    def swipe_find(self, text, num=3):
        '''
        1、添加查找次数
        2、添加 查找文本 的输入参数
        3、添加隐式等待的动态设置
        :param text:
        :param num:
        :return:
        '''
        # 滑动查找元素
        # 优化 隐式等待，提高查找速度
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:

                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']

                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                duration = 2000

                self.driver.swipe(start_x, start_y, end_x, end_y, duration)

            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了 {i} 次，未找到")

    def test_addcontact(self):
        # name = "hogwarts03"
        # phonenum = "13100000003"
        name = self.fake.name()
        phonenum = self.fake.phone_number()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # done: 优化 滑动查找添加成员
        self.swipe_find('添加成员').click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # find_elemenets 会找到一个元素的列表[ele1,ele2]
        # self.driver.find_elements(MobileBy.XPATH, "//*[@text='必填']")[0].send_keys()
        # self.driver.find_elements(MobileBy.XPATH, "//*[@text='必填']")[1].send_keys()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'手机')]/..//android.widget.EditText").send_keys(phonenum)
        # 查找手机对应的输入框的另一种写法 //*[contains(@text,'手机')]/..//*[@text='必填']
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # 断言  获取 toast 完成判断
        # sleep(2)
        # page_source 打印页面的xml 布局
        # print(self.driver.page_source)
        # toast 展示 2-3 秒自动消失，使用find_element 会在隐式等待的时间内自动的查找这个元素
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute('text')
        # result = self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成功']").get_attribute('text')
        assert '添加成功' == result
