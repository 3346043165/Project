import time
import pytest
import os
import psutil
from selenium import webdriver
from Page.page import Page
from Page.page1 import Page1
from Page.page2 import Page2
from Page.page3 import Page3
from uilts.ui_config1 import get_browser
@pytest.fixture()
def driver(get_browser):
    driver=get_browser
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()
    # 杀死浏览器进程
    kill_browser_processes()
def kill_browser_processes():
    """杀死浏览器相关进程"""
    browsers = ['chrome', 'firefox', 'edge']
    killed = False

    for process in psutil.process_iter():
        try:
            process_name = process.name().lower()  # 使用 name() 方法
            pid = process.pid  # 使用 pid 属性
            for browser in browsers:
                if browser in process_name:
                    print(f"Killing browser process: {process_name} (PID: {pid})")
                    process.kill()
                    killed = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if killed:
        print("Browser processes killed successfully")
    else:
        print("No browser processes found to kill")
#登录
def test_01_login(driver):
    po=Page(driver)
    po.louji_A3mall()

#新增代理商
def test_02_address(driver):
    po=Page1(driver)
    po.louji_A3mall()
    time.sleep(3)
    po.louji1_A3mall()

#新增地区
def test_03_search(driver):
    po=Page2(driver)
    po.louji_A3mall()
    po.louji2_A3mall()

#修改地区
def test_04_product(driver):
    po=Page3(driver)
    po.louji_A3mall()
    po.louji3_A3mall()