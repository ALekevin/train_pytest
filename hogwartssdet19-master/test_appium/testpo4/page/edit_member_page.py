"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/4 4:14 下午'
"""
# 编辑成员页
# from test_appium.testpo1.page.add_member_page import AddMemberPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.testpo4.page.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, name, phonenum):
        # input name
        # input phonenum
        # click 保存
        self.find_and_sendkeys(MobileBy.XPATH,
                               "//*[contains(@text,'姓名')]/../android.widget.EditText", name)
        self.find_and_sendkeys(MobileBy.XPATH,
                               "//*[contains(@text,'手机')]/..//android.widget.EditText", phonenum)
        # 查找手机对应的输入框的另一种写法 //*[contains(@text,'手机')]/..//*[@text='必填']
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")

        from test_appium.testpo2.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)
