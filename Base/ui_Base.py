import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
class Base():
    #初始化事件
    def __init__(self,driver):
        self.driver=driver
    #网址事件
    def open_ulr(self,ulr):
        self.driver.get(ulr)
    #强制等待事件  使整个程序无条件停止
    def sleep(self,s):
        time.sleep(s)
    #定位元素事件
    def find_element(self,loc):
        t=time.strftime('%Y%m%d%H%M%S',time.localtime())
        try:
            #显示等待事件  给了最大等待时间20秒  每0.5秒找一次，直到20秒报错
            WebDriverWait(self.driver,20,0.5).until(lambda driver:self.driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as f:
            self.driver.save_screenshot('cuo'+t+'.png')
    # 隐式等待事件  给整个一个最大等待时间
    def implicitly_wait(self,x):
        self.driver.implicitly_wait(x)
    def WebDriverWait(self,x,y,loc):
        return WebDriverWait(self.driver,x,y).until(lambda driver: self.driver.find_element(*loc).is_displayed())
    #点击事件
    def click(self,loc):
        self.find_element(loc).click()
    #输入事件
    def send_keys(self,loc,info):
        self.find_element(loc).send_keys(info)
    #鼠标事件
    def ActionChains(self,loc):
        ActionChains(self.driver).double_click(self.find_element(loc)).perform()
    #键盘事件
    def keys(self,loc):
        self.find_element(loc).send_keys(Keys.ENTER)
    #下拉框选择
    def select(self,loc,x):
        a=Select(self.find_element(loc))
        a.select_by_value(x)
    #文本事件
    def text(self,loc):
        return self.find_element(loc).text
    #切换页面
    def window_handles(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
    #弹框处理
    def alert(self):
        self.driver.switch_to.alert.accept()
    #iframe处理
    def frame(self,loc):
        self.driver.switch_to.frame(self.find_element(loc))
    #iframe退出处理
    def tui(self):
        self.driver.switch_to.default_content()
    #滚动条
    def execute_script(self,x):
        self.driver.execute_script(f'window.scrollTo(0,{x})')
    #浏览器放大事件
    def maximize_window(self):
        self.driver.maximize_window()
    #浏览器缩小事件
    def minimize_window(self):
        self.driver.minimize_window()
    #浏览器退出事件
    def quit(self):
        self.driver.quit()