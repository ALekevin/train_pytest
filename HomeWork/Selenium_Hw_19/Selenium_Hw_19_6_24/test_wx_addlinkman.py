import configparser
import os
from time import sleep

import allure
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWxlinkname:
    def get_config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join("C:",os.environ['HOME'], 'iselenium.ini'))
        return config

    def tearDown(self):
        self.driver.quit()

    def setup(self):
        print('开始测试')
        config = self.get_config()

        # 控制是否采用无界面形式运行自动化测试
        try:
            using_headless = os.environ["using_headless"]
        except KeyError:
            using_headless = None
            print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')

        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print('使用无界面方式运行')
            chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'),
                                       options=chrome_options)

    @allure.step('删除添加联系人')
    def teardown(self):
        print('结束测试')
        self.driver.find_element(By.XPATH,"//*[text()='lekaixin1']/../..//*[@class='ww_checkbox']").click()
        self.driver.find_element(By.XPATH, "//*[@class='ww_operationBar']//a[text()='删除']").click()
        self.driver.find_element(By.XPATH, "//*[text()='确认']").click()
        self.driver.find_element(By.XPATH, "//*[text()='删除成功']")
        self.driver.close()


    # def test_login(self):
    #     self.opt = webdriver.ChromeOptions()
    #     self.opt.debugger_address = '127.0.0.1:9222'
    #     self.driver = webdriver.Chrome(options=self.opt)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #     with open('cookies.yaml', 'w', encoding='UTF-8') as f:
    #         yaml.safe_dump(self.driver.get_cookies(), f)


    def test_add_linkname(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        with open('cookies.yaml', 'r', encoding='UTF-8') as f:
            cookies=yaml.safe_load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_id('menu_contacts').click()
        sleep(2)
        self.driver.find_element(By.XPATH,"//*[@class='ww_operationBar']//a[text()='添加成员']").click()
        self.driver.find_element(By.ID,"username").send_keys('lekaixin1')
        self.driver.find_element(By.ID,"memberAdd_english_name").send_keys('kevin1')
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys('lkx1')
        self.driver.find_element(By.XPATH,"//*[text()='男']").click()
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys('17711440200')
        self.driver.find_element(By.ID,"memberAdd_telephone").send_keys('8433053')
        self.driver.find_element(By.ID,"memberAdd_mail").send_keys('260317441@qq.com')
        self.driver.find_element(By.ID,"memberEdit_address").send_keys('地球')
        self.driver.find_element(By.ID,"memberAdd_title").send_keys('测试工程师')
        self.driver.find_element(By.XPATH,"//*[text()='普通成员']").click()
        self.driver.find_element(By.XPATH,"//*[@class='js_member_editor_form']/div[3]/*[@class='qui_btn ww_btn js_btn_save']").click()
        # self.driver.find_elements(By.XPATH, "//*[text()='保存成功']")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[text()='保存成功']")))
        sleep(5)
        self.driver.save_screenshot('./result/a.png')
        allure.attach.file('./result/a.png',attachment_type=allure.attachment_type.PNG)
