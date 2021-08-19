# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import os
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from faker import Faker
from selenium.common.exceptions import NoSuchElementException
from pytest_testconfig import config

class TestAddMember:
    def setup_class(self):
        self.faker = Faker('zh_CN')

    def setup(self):
        caps = {}
        appium_server_url = config['appium_server_url']
        caps['platformName'] = config['caps']['platformName']
        caps['udid'] = config['caps']['udid']
        caps['deviceName'] = config['caps']['deviceName']
        caps['appPackage'] = config['caps']['appPackage']
        caps['appActivity'] = config['caps']['appActivity']
        caps['automationName'] = config['caps']['automationName']
        caps['noReset'] = config['caps']['noReset']
        caps['ensureWebviewsHavePages'] = config['caps']['ensureWebviewsHavePages']
        # caps['app'] = f'{os.path.abspath(os.curdir)}/app/ContactManager.apk'

        self.driver = webdriver.Remote(appium_server_url, caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def swipe_find(self, text, num=3):
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
                start_x = int(width * 0.5)
                start_y = int(height * 0.8)
                end_x = int(width * 0.5)
                end_y = int(height * 0.2)
                duration = 2000
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == (num - 1):
                raise NoSuchElementException(f"找了{i}次 未找到")

    def test_add_member(self):
        name=self.faker.name()
        phone=self.faker.phone_number()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.swipe_find('添加成员').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='姓名　']/..//android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机　']/..//android.widget.EditText").send_keys(phone)
        self.swipe_find('保存').click()
        # sleep(1)
        # print(self.driver.page_source)
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        result1 = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'添加成功')]").text
        assert result == "添加成功"
        assert result1 == "添加成功"
