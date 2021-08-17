"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/4 4:12 下午'
"""
# 通讯录页面
from test_appium.testpo3.page.add_member_page import AddMemberPage
from test_appium.testpo3.page.base_page import BasePage


class AddressListPage(BasePage):

    def goto_addmemberpage(self):
        # click 添加成员
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)
