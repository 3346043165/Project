import pytest
import logging
import os
import requests
import yaml

with open(r"D:\shixunyi\atee\yongli\config\test_data.yaml", "r", encoding="utf-8") as f:
    datas = yaml.safe_load(f)
def rend_du():
    with open("rend.yaml","r",encoding="utf-8") as f:
        datas=yaml.safe_load(f)
        return datas
class Testui():
    token=""
    def setup_class(self):
        logging.info("准备资源")
    def teardown_class(self):
        logging.info("结束资源")
    #登录
    def test_01_login(self):
        login_data = datas["login"]  # 获取login的配置
        url = login_data["url"]
        data = login_data["data"]
        headers = login_data["headers"]
        response = requests.post(url=url, json=data, headers=headers)
        print(response .json())
        Testui.token=response .json()["token"]
        assert  response .json()['msg']=='登录成功'
        assert response .status_code==200
        assert 'token' in response .json()
        assert len(response.json()['token']) > 0
    #新增代理商
    # @pytest.mark.parametrize("data1",rend_du())
    def test_02_address(self):
        register_data = datas["agent"]  # 获取agent的配置
        url = register_data["url"]
        data = register_data["data"]
        headers = register_data["headers"]
        response= requests.post(url=url, json=data, headers=headers)
        print(response .json())
        logging.info(response)
        assert  '用户名已存在'==response .json()['msg']
        assert response.status_code == 200, f"期望状态码200，实际得到{response.status_code}"
    #新增地区
    def test_add_region_duplicate_name(self):
        register_data = datas["region"]  # 获取region的配置
        url = register_data["url"]
        data = register_data["data"]
        headers = register_data["headers"]
        headers["token"] = Testui.token  # 添加token
        add_region_response = requests.post(url=url, json=data, headers=headers)
        print(add_region_response.json())
        logging.info(add_region_response)
        assert  add_region_response.status_code==200
        assert '该地区名已存在' == add_region_response.json()['msg']
    #代理商列表
    def test_log_list(self):
        register_data = datas["list"]  # 获取list的配置
        url = register_data["url"]
        data = register_data["data"]
        headers = register_data["headers"]
        headers["token"] = Testui.token  # 添加token
        response_data = requests.post(url=url, json=data, headers=headers)
        print(response_data .json())
        logging.info(response_data.json())
        assert  response_data.status_code==200
    #修改地区列表
    def test_04_product(self):
        register_data = datas["update"]  # 获取update的配置
        url = register_data["url"]
        data = register_data["data"]
        headers = register_data["headers"]
        headers["token"] = Testui.token  # 添加token
        r = requests.post(url=url, json=data, headers=headers)
        print(r.json())
        logging.info(r.json())
        assert  r.status_code==200
        assert '服务端错误' == r.json()['msg']