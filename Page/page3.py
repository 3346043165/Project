# import time
#
# from selenium.webdriver.common.by import By
# from Page.page1 import Page
# class Page3(Page):
#     shouye_loc=(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/ul/li[3]/ul/li[1]')
#     def shouye(self):
#         self.click(self.shouye_loc)
#     shousuo_loc=(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[3]/table/tbody/tr[1]/td[6]/div/button/span')
#     def sousuo(self):
#         self.click(self.shousuo_loc)
#     dianji_loc=(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/input')
#     def dianji(self):
#         self.send_keys(self.dianji_loc,'的爱第哇')
#     touxiang_loc=(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/input')
#     def touxiang(self):
#         self.send_keys(self.touxiang_loc,'89696')
#     jiaru_loc=(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div[2]/form/div[3]/div/button/span')
#     def jiaru(self):
#         self.click(self.jiaru_loc)
#     def louji3_A3mall(self):
#         self.shouye()
#         time.sleep(3)
#         self.sousuo()
#         time.sleep(3)
#         self.dianji()
#         time.sleep(7)
#         self.touxiang()
#         time.sleep(3)
#         self.jiaru()
#         time.sleep(3)

import time
from selenium.webdriver.common.by import By
from Page.page1 import Page

class Page3(Page):
    def __init__(self, driver):
        super().__init__(driver)  # 调用父类的__init__，loader已经在父类中初始化了
        # 直接从父类继承的loader加载元素，不需要再创建新的loader
        self.shouye_loc = self.loader.get_locator('product_page', 'shouye_menu')
        self.edit_button_loc = self.loader.get_locator('product_page', 'edit_button')
        self.name_input_loc = self.loader.get_locator('product_page', 'name_input')
        self.code_input_loc = self.loader.get_locator('product_page', 'code_input')
        self.submit_button_loc = self.loader.get_locator('product_page', 'submit_button')

    def click_shouye_menu(self):
        """点击商品菜单"""
        self.click(self.shouye_loc)

    def click_edit_button(self):
        """点击编辑按钮"""
        self.click(self.edit_button_loc)

    def fill_product_form(self, name='的爱第哇', code='89696'):
        """填写商品表单"""
        self.send_keys(self.name_input_loc, name)
        self.send_keys(self.code_input_loc, code)

    def click_submit_button(self):
        """点击提交按钮"""
        self.click(self.submit_button_loc)

    def louji3_A3mall(self, name='的爱第哇', code='89696'):
        """完整的商品编辑流程"""
        self.click_shouye_menu()
        time.sleep(3)
        self.click_edit_button()
        time.sleep(3)
        self.fill_product_form(name, code)
        time.sleep(7)
        self.click_submit_button()
        time.sleep(3)