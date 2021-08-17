"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/4 4:09 下午'
"""

# 主页面
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.testpo4.page.addresslist_page import AddressListPage
from test_appium.testpo4.page.base_page import BasePage


class MainPage(BasePage):
    _addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_addresslist(self):
        # click 通讯录
        self.find_and_click(*self._addresslist_element)
        return AddressListPage(self.driver)
