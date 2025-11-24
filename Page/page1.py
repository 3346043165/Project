import time

from selenium.webdriver.common.by import By
from Page.page import Page
# class Page1(Page):
#     dizhi_loc=(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/ul/li[2]/ul/li[2]')
#     def dizhi(self):
#         self.click(self.dizhi_loc)
#     tianjia_loc=(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/input')
#     tianjia_loc1=(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/input')
#     tianjia_loc2=(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/input')
#     tianjia_loc3=(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div/div/input')
#     tianjia_loc4=(By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[2]')
#     tianjia_loc5=(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/div[5]/div/div/input')
#     tianjia_loc6=(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/div[6]/div/div/input')
#     tianjia_loc7=(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/div[8]/div/button/span')
#     def tianjia(self):
#         self.send_keys(self.tianjia_loc,'fsefe')
#         self.send_keys(self.tianjia_loc1,'123456')
#         self.send_keys(self.tianjia_loc2,'123456')
#         self.click(self.tianjia_loc3)
#         self.click(self.tianjia_loc4)
#         self.send_keys(self.tianjia_loc5,'那么扣挖到')
#         self.send_keys(self.tianjia_loc6,'13029862439')
#         self.click(self.tianjia_loc7)
#     def louji1_A3mall(self):
#         self.dizhi()
#         time.sleep(2)
#         self.tianjia()
#         time.sleep(4)
class Page1(Page):  # 继承Page类
    def __init__(self, driver):
        super().__init__(driver)  # 调用父类的__init__，loader已经在父类中初始化了
        # 直接从父类继承的loader加载元素，不需要再创建新的loader
        self.address_menu_loc = self.loader.get_locator('address_page', 'address_menu')
        self.add_field1_loc = self.loader.get_locator('address_page', 'add_field1')
        self.add_field2_loc = self.loader.get_locator('address_page', 'add_field2')
        self.add_field3_loc = self.loader.get_locator('address_page', 'add_field3')
        self.dropdown_field_loc = self.loader.get_locator('address_page', 'dropdown_field')
        self.dropdown_option_loc = self.loader.get_locator('address_page', 'dropdown_option')
        self.add_field4_loc = self.loader.get_locator('address_page', 'add_field4')
        self.add_field5_loc = self.loader.get_locator('address_page', 'add_field5')
        self.submit_button_loc = self.loader.get_locator('address_page', 'submit_button')

    def click_address_menu(self):
        """点击地址管理菜单"""
        self.click(self.address_menu_loc)

    def fill_address_form(self, field1='fsefe', field2='123456', field3='123456',
                          field4='那么扣挖到', field5='13029862439'):
        """填写地址表单"""
        self.send_keys(self.add_field1_loc, field1)
        self.send_keys(self.add_field2_loc, field2)
        self.send_keys(self.add_field3_loc, field3)

        # 处理下拉框
        self.click(self.dropdown_field_loc)
        time.sleep(1)  # 等待下拉框展开
        self.click(self.dropdown_option_loc)

        self.send_keys(self.add_field4_loc, field4)
        self.send_keys(self.add_field5_loc, field5)

    def click_submit(self):
        """点击提交按钮"""
        self.click(self.submit_button_loc)

    def louji1_A3mall(self, field1='fsefe', field2='123456', field3='123456',
                        field4='那么扣挖到', field5='13029862439'):
        """完整的添加地址流程"""
        self.click_address_menu()
        time.sleep(2)
        self.fill_address_form(field1, field2, field3, field4, field5)
        self.click_submit()
        time.sleep(4)