from HomeWork.WX_Hw_4_18.Base import Testinit
from HomeWork.WX_Hw_4_18.wx_main import main_page


class TestAddMember:
    def test_add_member(self):
        test_init=Testinit()
        #实例化主页
        test_init.mainpage = main_page()
                   #主页面    #点击添加用户按钮   #添加用户保存   #获取用户列表信息
        test_init.mainpage.goto_add_member().add_member().get_member_list()