"""
__author__ = 'jaxon'
__time__ = '2021/6/27 2:47 下午'
__desc__ = ''
"""

# 主页
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.po.basepage import BasePage
from test_selenium.po.contact_page import ContactPage


class MainPage(BasePage):
    _CONTACT = (By.ID,"menu_contacts")

    # 跳转至通讯录页面
    def goto_contact(self):
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=opt)
        # self.driver.implicitly_wait(10)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # self.driver.find_element_by_id("menu_contacts").click()
        self.find_and_click(*self._CONTACT)

        return ContactPage(self.driver)