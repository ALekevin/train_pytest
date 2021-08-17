"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/1 8:50 下午'
"""
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# pip install appium-python-client
from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.LaunchSplashActivity"
caps["deviceName"] = "hogwarts"
caps["noReset"] = "true"
# 至关重要的一行  与appium 服务建立连接，并传递一个caps 字典对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
el1.click()
el2 = driver.find_element_by_id("com.tencent.wework:id/igk")
el2.click()
el3 = driver.find_element_by_id("com.tencent.wework:id/gy9")
el3.send_keys("hogwarts")

driver.quit()
