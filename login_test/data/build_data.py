import json


def build_data():
    with open('D:\code\login_test\data\login_data.json', encoding='utf-8') as f:
        data_list = json.load(f)
    new_list = []
    for data in data_list:
        username = data.get('username')
        password = data.get('password')
        expect = data.get('expect')
        new_list.append((username,password,expect))
    return new_list
print(build_data())

