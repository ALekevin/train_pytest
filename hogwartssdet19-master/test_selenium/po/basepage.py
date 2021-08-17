"""
__author__ = 'jaxon'
__time__ = '2021/6/27 4:03 下午'
__desc__ = ''
"""
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,driver_base: WebDriver = None):
        # 避免driver重复初始化
        if driver_base is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            print("实例化driver")
        else:
            self.driver = driver_base

    def find(self,by,locator):
        ele = self.driver.find_element(by,locator)
        return ele

    def finds(self,by,locator):
        eles = self.driver.find_elements(by,locator)
        return eles

    def find_and_click(self,by,locator):
        ele = self.driver.find_element(by,locator)
        ele.click()

    def wait_for_click(self,locator, timeout=10):
        element:WebElement = WebDriverWait(self.driver,timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        element.click()
        return element

    def close_driver(self):
        self.driver.close()




