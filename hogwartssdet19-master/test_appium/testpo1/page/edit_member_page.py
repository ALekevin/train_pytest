"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/4 4:14 下午'
"""
# 编辑成员页
# from test_appium.testpo1.page.add_member_page import AddMemberPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class EditMemberPage(object):
    def __init__(self, driver: WebDriver):
        # 将上个页面的driver传递过来
        self.driver = driver

    def edit_member(self, name, phonenum):
        # input name
        # input phonenum
        # click 保存
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'手机')]/..//android.widget.EditText").send_keys(phonenum)
        # 查找手机对应的输入框的另一种写法 //*[contains(@text,'手机')]/..//*[@text='必填']
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

        from test_appium.testpo1.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)
