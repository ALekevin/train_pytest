from HomeWork.WX_Hw_4_18.wx_add_member import add_member_page
from HomeWork.WX_Hw_4_18.wx_contact import contact_page


class main_page:
    # 点击通讯录按钮
    def goto_contact(self):
        '''

        :return:
        '''
        return contact_page()

    # 点击添加成员按钮
    def goto_add_member(self):
        '''

        :return:
        '''
        return add_member_page()
