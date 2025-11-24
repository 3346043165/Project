import time
import pytest
import psutil
import subprocess
import platform
from selenium import webdriver
from uilts.ui_config1 import get_browser
from config_loader import config


# 全局夹具 - 浏览器实例
@pytest.fixture(scope="session")
def browser_driver():
    """全局浏览器驱动实例"""
    driver = get_browser()
    driver.maximize_window()
    yield driver
    # 清理操作
    driver.close()
    driver.quit()
    kill_browser_processes()


# 函数级夹具 - 每个测试函数使用的driver
@pytest.fixture()
def driver(browser_driver):
    """每个测试函数使用的driver夹具"""
    yield browser_driver


# 页面对象夹具
@pytest.fixture()
def page(driver):
    """Page页面对象夹具"""
    from Page.page import Page
    return Page(driver)


@pytest.fixture()
def page1(driver):
    """Page1页面对象夹具"""
    from Page.page1 import Page1
    return Page1(driver)


@pytest.fixture()
def page2(driver):
    """Page2页面对象夹具"""
    from Page.page2 import Page2
    return Page2(driver)


@pytest.fixture()
def page3(driver):
    """Page3页面对象夹具"""
    from Page.page3 import Page3
    return Page3(driver)


# 环境配置夹具
@pytest.fixture()
def environment_config():
    """环境配置夹具"""
    from constants import ENV_CONFIG, BASE_URL, USERNAME, PASSWORD
    return {
        'config': ENV_CONFIG,
        'base_url': BASE_URL,
        'username': USERNAME,
        'password': PASSWORD
    }


# 测试数据夹具
@pytest.fixture()
def test_data():
    """测试数据夹具"""
    from constants import TEST_DATA
    return TEST_DATA


# 登录状态夹具
@pytest.fixture()
def logged_in_session(driver):
    """已登录状态的夹具"""
    from Page.page import Page
    from constants import USERNAME, PASSWORD

    po = Page(driver)
    po.louji_A3mall(USERNAME, PASSWORD)
    yield driver
    # 可选：登出操作
    # po.logout()


# 工具函数
def kill_browser_processes():
    """杀死浏览器相关进程"""
    browser_config = config.get_browser_config()
    browser_name = browser_config.get('name', 'chrome').lower()

    # 根据浏览器名称确定要杀死的进程
    if browser_name == 'chrome':
        processes = ['chrome', 'chromedriver']
    elif browser_name == 'firefox':
        processes = ['firefox', 'geckodriver']
    elif browser_name == 'edge':
        processes = ['msedge', 'msedgedriver']
    else:
        processes = ['chrome', 'firefox', 'edge', 'iexplore']

    killed = False
    system = platform.system().lower()

    if system == "windows":
        # Windows系统使用taskkill
        for process in processes:
            try:
                subprocess.run(f"taskkill /f /im {process}.exe", shell=True, capture_output=True)
                print(f"Killed process: {process}")
                killed = True
            except Exception as e:
                print(f"Error killing {process}: {e}")
    else:
        # Linux/macOS系统使用pkill
        for process in processes:
            try:
                subprocess.run(f"pkill -f {process}", shell=True, capture_output=True)
                print(f"Killed process: {process}")
                killed = True
            except Exception as e:
                print(f"Error killing {process}: {e}")

    if not killed:
        print("No browser processes found to kill")


# 可选：钩子函数
def pytest_configure(config):
    """pytest配置钩子"""
    print("=== A3mall UI自动化测试开始 ===")


def pytest_unconfigure(config):
    """pytest清理钩子"""
    print("=== A3mall UI自动化测试结束 ===")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """测试报告钩子，用于失败时截图"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # 失败时截图逻辑
        screenshot_config = config.get('screenshot', {})
        if screenshot_config.get('on_failure', True):
            try:
                # 获取driver实例
                driver_fixture = item.funcargs.get('driver') or item.funcargs.get('browser_driver')
                if driver_fixture:
                    screenshot_path = config.get('screenshot.save_path', './screenshots/')
                    import os
                    os.makedirs(screenshot_path, exist_ok=True)
                    filename = f"{item.name}_{time.strftime('%Y%m%d_%H%M%S')}.png"
                    full_path = os.path.join(screenshot_path, filename)
                    driver_fixture.save_screenshot(full_path)
                    print(f"Screenshot saved: {full_path}")
            except Exception as e:
                print(f"Failed to take screenshot: {e}")