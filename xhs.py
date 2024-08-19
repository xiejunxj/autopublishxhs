import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import Config


def login():
    Config.Browser.get("https://creator.xiaohongshu.com/login")
    # 访问登陆页面
    time.sleep(5)
    Config.Browser.switch_to.active_element.send_keys(Config.phone)
    Config.Browser.switch_to.active_element.send_keys(Keys.TAB)
    time.sleep(3)
    Config.Browser.execute_script(f'document.querySelector(".css-uyobdj").click()')
    verifyCode = ''
    print("please input verify code\n")
    while True:
        verifyCode = input()
        if len(verifyCode) == 6:
            break
    Config.Browser.execute_script("document.querySelector('.css-19z0sa3.css-1ge5flv.dyn').value = '%s';" % (verifyCode))
    time.sleep(2)
    Config.Browser.execute_script(
        'document.querySelector(".css-19z0sa3.css-1ge5flv.dyn").dispatchEvent(new Event("input"))')
    time.sleep(1)
    js_login_click = f'document.querySelector(".css-1jgt0wa.css-kyhkf6.dyn").click()'
    Config.Browser.execute_script(js_login_click)
    print("success login")
    time.sleep(3)

def uploadNote():
    if Config.Browser.current_url != "https://creator.xiaohongshu.com/publish/publish":
        Config.Browser.get("https://creator.xiaohongshu.com/publish/publish")
    try:
        WebDriverWait(Config.Browser, 10, 0.2).until(
            lambda x: x.find_element(By.CSS_SELECTOR, "div.tab:nth-child(2)")).click()
    except TimeoutException:
        print("网页好像加载失败了！请重试！")
    #  上传图片
    Config.Browser.find_element(By.CSS_SELECTOR, ".upload-wrapper > div:nth-child(1) > input:nth-child(1)").send_keys(
        Config.PathImage)
    Config.Browser.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys(Config.title)
    Config.Browser.find_element(By.CSS_SELECTOR, "#post-textarea").send_keys(Config.describe)
    print("等待资源上传……")
    time.sleep(10)
    create_js = f'return document.querySelector(".publishBtn")'
    Config.Browser.execute_script(create_js).click()
    print("发布成功！")
    print("等待页面返回！")
    time.sleep(5)
def init():
    # 谷歌浏览器
    Config.Browser = webdriver.Chrome()
    Config.PathImage = f'C:\\Users\\I584846\\Downloads\\a.jpg'
    Config.title = "我的第一个笔记"
    Config.describe = "我的第一个笔记"


def start():
    try:
        # 初始化
        init()
        #   登录
        login()
        # 上传笔记
        uploadNote()
    except KeyboardInterrupt:
        print("\nBye!")
    except Exception as e:
        print(f"发生了一些错误：\n{e}")
