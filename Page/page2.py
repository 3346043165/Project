# import time
#
# from selenium.webdriver.common.by import By
# from Page.page1 import Page
# class Page2(Page):
#     shouye_loc=(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/ul/li[3]/ul/li[2]')
#     def shouye(self):
#         self.click(self.shouye_loc)
#     shousuo_loc=(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/input')
#     def sousuo(self):
#         self.send_keys(self.shousuo_loc,"音乐耳机")
#     dianji_loc=(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/input')
#     def dianji(self):
#         self.send_keys(self.dianji_loc,'25523')
#     touxiang_loc=(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div[2]/form/div[3]/div/button')
#     def touxiang(self):
#         self.click(self.touxiang_loc)
#     def louji2_A3mall(self):
#         self.shouye()
#         time.sleep(3)
#         self.sousuo()
#         time.sleep(3)
#         self.dianji()
#         time.sleep(7)
#         self.touxiang()
#         time.sleep(3)


import time
from selenium.webdriver.common.by import By
from Page.page1 import Page

class Page2(Page):
    def __init__(self, driver):
        super().__init__(driver)  # 调用父类的__init__，loader已经在父类中初始化了
        # 直接从父类继承的loader加载元素，不需要再创建新的loader
        self.shouye_loc = self.loader.get_locator('search_page', 'shouye_menu')
        self.search_input_loc = self.loader.get_locator('search_page', 'search_input')
        self.code_input_loc = self.loader.get_locator('search_page', 'code_input')
        self.search_button_loc = self.loader.get_locator('search_page', 'search_button')

    def click_shouye_menu(self):
        """点击首页菜单"""
        self.click(self.shouye_loc)

    def fill_search_form(self, keyword="音乐耳机", code="25523"):
        """填写搜索表单"""
        self.send_keys(self.search_input_loc, keyword)
        self.send_keys(self.code_input_loc, code)

    def click_search_button(self):
        """点击搜索按钮"""
        self.click(self.search_button_loc)

    def louji2_A3mall(self, keyword="音乐耳机", code="25523"):
        """完整的搜索流程"""
        self.click_shouye_menu()
        time.sleep(3)
        self.fill_search_form(keyword, code)
        time.sleep(3)
        self.click_search_button()
        time.sleep(3)