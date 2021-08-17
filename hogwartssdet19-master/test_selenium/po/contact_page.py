"""
__author__ = 'jaxon'
__time__ = '2021/6/27 2:47 下午'
__desc__ = ''
"""

# 通讯录页面
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.po.add_member_page import AddMemberPage
from test_selenium.po.basepage import BasePage


class ContactPage(BasePage):
    _ADDMEMBER = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _NAMES = (By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")

    # 点击添加成员
    def click_add_member(self):
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=opt)
        # self.driver.implicitly_wait(10)
        # ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ele))
        self.wait_for_click(self._ADDMEMBER)
        # self.driver.find_element_by_css_selector(".ww_operationBar .js_add_member").click()
        return AddMemberPage(self.driver)

    # 获取成员信息，进行返回
    def get_member_name(self):
        sleep(1)
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=opt)
        name_list = []
        # eles = self.driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
        eles = self.finds(*self._NAMES)
        for value in eles:
            name_list.append(value.get_attribute("title"))
        return name_list