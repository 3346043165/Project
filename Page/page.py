# import time
# from Base.ui_Base import Base
# from selenium.webdriver.common.by import By
# class Page(Base):
#     dy1_loc=(By.XPATH,"/html/body/div/div/div/div/div")
#     def dy1(self):
#         return self.text(self.dy1_loc)
#     username_loc=(By.XPATH,'/html/body/div/div/div/form/div[1]/div/div/input')
#     def username(self):
#         self.send_keys(self.username_loc,'admin')
#     password_loc=(By.XPATH,'/html/body/div/div/div/form/div[2]/div/div/input')
#     def password(self):
#         self.send_keys(self.password_loc,'qwe123123')
#     loginbtn_loc=(By.XPATH,'/html/body/div/div/div/form/div[3]/div/button/span')
#     def loginbtn(self):
#         self.click(self.loginbtn_loc)
#     def louji_A3mall(self):
#         self.open_ulr("http://10.59.9.21/dist#/login")
#         print(self.dy1())
#         self.username()
#         self.password()
#         time.sleep(3)
#         self.loginbtn()
#         time.sleep(3)
import time
from Base.ui_Base import Base
from selenium.webdriver.common.by import By
from Page.element_loader import ElementLoader
class Page(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.loader = ElementLoader()
        # 从UI Map Tree加载所有元素 - 正确的写法
        self.title_loc = self.loader.get_locator('login_page', 'title')
        self.username_loc = self.loader.get_locator('login_page', 'username_input')
        self.password_loc = self.loader.get_locator('login_page', 'password_input')
        self.loginbtn_loc = self.loader.get_locator('login_page', 'login_button')

    def get_title(self):
        return self.text(self.title_loc)

    def input_username(self, username='admin'):
        self.send_keys(self.username_loc, username)

    def input_password(self, password='qwe123123'):
        self.send_keys(self.password_loc, password)

    def click_login(self):
        self.click(self.loginbtn_loc)

    def louji_A3mall(self):
        self.open_ulr("http://10.59.9.21/dist#/login")
        print(self.get_title())
        self.input_username()
        self.input_password()
        time.sleep(3)
        self.click_login()
        time.sleep(3)