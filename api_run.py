import os

import pytest
from uilts.rizhi import login
from uilts.fasong import fs
if __name__ == '__main__':
    #日志
    login()
    #普通报告
    # pytest.main([r'D:\实训一\atee\yongli\Case\api_case.py','-s','--html=./index.html'])
    #allure报告
    pytest.main([
        "./Case/api_case.py",  # 相对路径（确保Case文件夹与api_run.py同级）
        "-s",  # 显示打印信息
        "--alluredir", "./allure-results",  # 生成Allure数据的目录（名称简化，避免拼写错误）
        "--clean-alluredir"  # 清空旧数据
    ])
    # os.system('allure generate allureapibaogao -o allureapibg --clean')
