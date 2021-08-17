"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/4 4:12 下午'
"""
# 通讯录页面
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from test_appium.testpo1.page.add_member_page import AddMemberPage


class AddressListPage(object):
    def __init__(self, driver: WebDriver):
        # 将上个页面的driver传递过来
        self.driver = driver

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

    def goto_addmemberpage(self):
        # click 添加成员
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)
