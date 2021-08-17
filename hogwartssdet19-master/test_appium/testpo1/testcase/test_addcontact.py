"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/4 4:15 下午'
"""
from faker import Faker

from test_appium.testpo1.page.app import App


class TestContact:
    def setup_class(self):
        self.fake = Faker('zh_CN')

    def setup(self):
        # 启动应用
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.quit()

    def test_addcontact(self):
        name = self.fake.name()
        phonenum = self.fake.phone_number()
        result = self.main.goto_addresslist().goto_addmemberpage(). \
            click_addmember_menual().edit_member(name, phonenum).get_result()
        assert '添加成功' == result
