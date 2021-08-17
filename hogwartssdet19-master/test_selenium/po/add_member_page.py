"""
__author__ = 'jaxon'
__time__ = '2021/6/27 2:48 下午'
__desc__ = ''
"""


# 添加成员详情页
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.po.basepage import BasePage


class AddMemberPage(BasePage):
    _NAME = (By.ID,"username")
    _ACCTID = (By.ID,"memberAdd_acctid")
    _MAIL = (By.ID,"memberAdd_mail")
    _SAVE = (By.CSS_SELECTOR,".js_btn_save")

    # 添加成员信息
    def edit_member(self,name,contact_id,mail):
        # 局部导入，解决循环导入问题
        from test_selenium.po.contact_page import ContactPage
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=opt)
        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id("username").send_keys("张三1")
        # self.driver.find_element_by_id("memberAdd_acctid").send_keys("1236781")
        # self.driver.find_element_by_id("memberAdd_mail").send_keys("12300011@qq.com")
        # self.driver.find_element_by_css_selector(".js_btn_save").click()
        self.find(*self._NAME).send_keys(name)
        self.find(*self._ACCTID).send_keys(contact_id)
        self.find(*self._MAIL).send_keys(mail)
        self.find_and_click(*self._SAVE)
        return ContactPage(self.driver)
