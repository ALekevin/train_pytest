"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/4 4:13 下午'
"""
# from test_appium.testpo1.page.edit_member_page import EditMemberPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class AddMemberPage(object):
    def __init__(self, driver: WebDriver):
        # 将上个页面的driver传递过来
        self.driver = driver

    def click_addmember_menual(self):
        # click 手动输入添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        from test_appium.testpo1.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

    def get_result(self):
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute('text')
        return result
