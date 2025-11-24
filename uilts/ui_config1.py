import pytest
from selenium import webdriver


@pytest.fixture(params=['edge', 'chrome', 'firefox'], scope="module")
def get_browser(request):
    browser_name = request.param
    driver = None
    if browser_name == 'edge':
        driver = webdriver.Chrome()
    elif browser_name == 'chrome':
        driver = webdriver.Edge()
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"不支持的浏览器：{browser_name}")
    # 最大化窗口
    driver.maximize_window()
    # yield 关键字将 fixture 分为 setup 和 teardown 部分
    yield driver
    driver.quit()