"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/4 4:13 下午'
"""
# from test_appium.testpo1.page.edit_member_page import EditMemberPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.testpo4.page.base_page import BasePage


class AddMemberPage(BasePage):

    def click_addmember_menual(self):
        # click 手动输入添加
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        from test_appium.testpo2.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

    def get_result(self):
        # result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute('text')
        result = self.get_toast_text()
        return result
