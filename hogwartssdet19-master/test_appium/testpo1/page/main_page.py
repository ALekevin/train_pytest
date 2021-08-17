"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/4 4:09 下午'
"""

# 主页面
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.testpo1.page.addresslist_page import AddressListPage


class MainPage(object):
    def __init__(self, driver: WebDriver):
        # 将上个页面的driver传递过来
        self.driver = driver

    def goto_addresslist(self):
        # click 通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)
