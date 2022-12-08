import json
import os
from tpsh_test_mode1.config import DIR_PATH, HOST
from selenium import webdriver


def read_json(filename, key):
    filepath = DIR_PATH + os.sep + "data" + os.sep + filename
    arr = []
    with open(filepath, 'r', encoding='utf-8') as f:
        # print(json.load(f))
        for data in json.load(f).get(key):
            # print(data)
            arr.append(tuple(data.values())[1:])
        return arr

# 批量导入数据
def read_json_all(filename):
    filepath = DIR_PATH + os.sep + "data" + os.sep + filename
    arr=[]
    with open(filepath,'r',encoding='utf-8') as f:
        for data in json.load(f).values():
            arr.append(tuple(data[0].values())[1:])
        return arr
            # a = data[0].values()
            # print(list(a))
            # print(type(a))
            # print(type(data[0]))

class Driver_GET:
    __web_driver = None

    @classmethod
    def get_driver(cls):
        if cls.__web_driver is None:
            cls.driver = webdriver.Chrome(r"D:\code\dirver\chromedriver.exe")
            cls.driver.get(HOST)
            cls.driver.maximize_window()
        return cls.driver

if __name__ == '__main__':
    # read_json('web_login_err.json',"login_1")
    # print(read_json_all('web_login_err.json',""))
    a = read_json_all('web_login_err.json')
    print(a)