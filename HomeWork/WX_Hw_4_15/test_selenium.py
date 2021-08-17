from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testweb:
    def test_web(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, "menu_contacts").click()
        cookies = self.driver.get_cookies()
        with open('cookies.yml', 'w', encoding='UTF-8') as f:
            yaml.dump(cookies,f)
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        cookies_data=yaml.safe_load(open('cookies.yml', encoding='UTF-8'))
        for cookie in cookies_data:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.ID, "menu_contacts").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//*[@class='ww_operationBar']//a[text()='添加成员']").click()
        self.driver.find_element(By.ID, "username").send_keys("lekaixin")
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys("kevin")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("lkx")
        self.driver.find_element(By.XPATH, "//*[text()='女']").click()
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys('13647912839')
        self.driver.find_element(By.ID, "memberAdd_telephone").send_keys('8433053')
        self.driver.find_element(By.ID, "memberAdd_mail").send_keys('260317442@qq.com')
        self.driver.find_element(By.ID, "memberEdit_address").send_keys('成都')
        # self.driver.find_element(By.XPATH,"//*[text()='修改']").click()
        self.driver.find_element(By.ID, "memberAdd_title").send_keys('CEO')
        self.driver.find_element(By.XPATH, "//*[text()='上级']").click()
        self.driver.find_element(By.XPATH, "//*[text()='自定义 ']").click()
        self.driver.find_element(By.NAME, "extern_position").send_keys('CEO')
        self.driver.find_element(By.XPATH,
                                 "//*[@class='js_member_editor_form']/div[3]/*[@class='qui_btn ww_btn js_btn_save']").click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//*[text()='保存成功']")))
