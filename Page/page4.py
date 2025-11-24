import time

from selenium.webdriver.common.by import By
from Page.page1 import Page
class Page2(Page):
    shouye_loc=(By.XPATH,'/html/body/div[3]/div[2]/ul/li[1]/a')
    def shouye(self):
        self.click(self.shouye_loc)
    shousuo_loc=(By.CLASS_NAME,'search-input')
    def sousuo(self):
        self.send_keys(self.shousuo_loc,"音乐耳机")
    dianji_loc=(By.CLASS_NAME,'search-input-btn')
    def dianji(self):
        self.click(self.dianji_loc)
    touxiang_loc=(By.XPATH,'/html/body/div[5]/div[2]/div[2]/div[1]/ul/li/div[1]/span/a/img')
    def touxiang(self):
        self.click(self.touxiang_loc)
    jiaru_loc=(By.ID,'add-cart')
    def jiaru(self):
        self.click(self.jiaru_loc)
    gouwuche_loc=(By.CLASS_NAME,'nav-settcart')
    def gouwuche(self):
        self.click(self.gouwuche_loc)
    gouxian_loc=(By.NAME,'id[]')
    def gouxian(self):
        self.click(self.gouxian_loc)
    xiayibu_loc=(By.CLASS_NAME,'ask-btn')
    def xiayibu(self):
        self.click(self.xiayibu_loc)
    xuandizhi_loc=(By.ID,'address-3443')
    def xuandizhi(self):
        self.click(self.xuandizhi_loc)
    jiesuan_loc=(By.ID,'order-button')
    def jiesuan(self):
        self.click(self.jiesuan_loc)
    def louji2_A3mall(self):
        self.shouye()
        time.sleep(3)
        self.sousuo()
        time.sleep(3)
        self.dianji()
        time.sleep(7)
        self.touxiang()
        time.sleep(3)
        self.jiaru()
        time.sleep(3)
        self.gouwuche()
        time.sleep(3)
        self.gouxian()
        time.sleep(3)
        self.xiayibu()
        time.sleep(3)
        self.xuandizhi()
        time.sleep(3)
        self.jiesuan()
        time.sleep(3)