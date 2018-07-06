# -*- coding:utf-8 -*-

import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


username = "1060288813"
password = "MswGhm15890564996"


class Moments(object):
    def __init__(self):
        # 驱动配置
        server = "http://localhost:4723/wd/hub"
        #登录模式
        desired_caps = {
          "platformName": "Android",
          "deviceName": "MI_5s_Plus",
          "appPackage": "com.tencent.mm",
          "appActivity": ".ui.LauncherUI"
            }

        #不登录
        # desired_caps = {
        #     "platformName": "Android",
        #     "deviceName": "MI_5s_Plus",
        #     "appPackage": "com.tencent.mm",
        #     "appActivity": ".ui.LauncherUI",
        #     "noReset": True,
        # }
        self.driver = webdriver.Remote(server, desired_capabilities=desired_caps)
        self.wait = WebDriverWait(self.driver, 30)

    def login(self):
        """
        登陆微信
        :return:
        """
        dl = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/d1w")))
        dl.click()
        # 点击用qq号登陆
        qq = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/bwm")))
        qq.click()
        # passwd = self.driver.find_elements_by_id("com.tencent.mm:id/hx")
        # 输入账号
        user_passwd = self.driver.find_elements_by_id("com.tencent.mm:id/hx")
        user = user_passwd[0]
        passwd = user_passwd[1]
        user.set_text(username)
        # 输入密码
        passwd.set_text(password)
        # 点击登陆按钮
        submit = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/bwn")))
        submit.click()
        # 不匹配通讯录
        alk = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/alk")))
        alk.click()

    def enter(self):
        """注释部分是选择添加好友的方式，进行爬取某一个好友的朋友圈"""
        # #点击通讯录
        # address_list = self.wait.until(
        #     EC.presence_of_all_elements_located( (By.XPATH, "//*[@resource-id='com.tencent.mm:id/ayn']") ) )
        # address_list[1].click()
        # #选择加号
        # plus = self.wait.until(
        #     EC.presence_of_all_elements_located( (By.ID, "com.tencent.mm:id/gd") ) )
        # plus[0].click()
        # #添加朋友
        # plus_friend = self.wait.until(
        #     EC.presence_of_all_elements_located( (By.ID, "com.tencent.mm:id/ge") ) )
        # plus_friend[1].click()
        # #查找好友
        # search = self.wait.until(
        #     EC.presence_of_all_elements_located( (By.ID, "com.tencent.mm:id/hx") ) )
        # search[0].click()
        # search_friend = self.driver.find_elements_by_id( "com.tencent.mm:id/hx" )
        # user = search_friend[0]
        # user.set_text( "monotonewang" ).send_keys(Keys.ENTER)
        # search_result = self.wait.until(
        #     EC.presence_of_all_elements_located( (By.ID, "com.tencent.mm:id/j5") ) )
        # search_result[0].click()

        # 点击"发现"选项卡
        finds = self.wait.until(
            EC.presence_of_all_elements_located( (By.XPATH, "//*[@resource-id='com.tencent.mm:id/ayn']") ) )
        finds[2].click()
        # 进入朋友圈
        friend = self.wait.until( EC.presence_of_element_located( (By.ID, "com.tencent.mm:id/a9d") ) )
        friend.click()

    def crawl(self):
        flick_start_x = 300
        flick_start_y = 300
        flick_distance = 700
        while True:
            self.driver.swipe(flick_start_x, flick_start_y+flick_distance, flick_start_x, flick_start_y)
            self.get_page_info()

    def get_page_info(self):
        items = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@resource-id='com.tencent.mm:id/ddn']//android.widget.LinearLayout")))
        for item in items:
            try:
                # 昵称
                nickname = item.find_element_by_id("com.tencent.mm:id/apv").get_attribute("text")
                # 正文
                content = item.find_element_by_id("com.tencent.mm:id/deq").get_attribute("text")
                print("{}---{}".format(nickname, content.replace("\n", "")))
            except NoSuchElementException:
                pass

    def run(self):
        # 登陆微信
        self.login()
        #进入朋友圈
        self.enter()
        # 抓取信息模拟上滑
        self.crawl()


if __name__ == "__main__":
    m = Moments()
    m.run()