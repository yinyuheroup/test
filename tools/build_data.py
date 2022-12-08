import json


def build_add_data():
    with open('D:\code\data\data_1.json') as f:
        data = json.load(f)
        # print(data)
        return data
