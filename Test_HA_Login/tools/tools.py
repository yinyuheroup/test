import json
import os

from parameterized import parameterized


def read_json(key):
    # filepath = os.path.dirname(__file__)+os.sep+'Data'+os.sep+filename
    filepath = r'C:\Users\TEST1\PycharmProjects\pythonProject\Test_HA_Login\tools\Data\login_data.json'
    arr = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for i in json.load(f).get(key):
            # print(i)
            arr.append(tuple(i.values())[1:])
        return arr


if __name__ == '__main__':
    print(read_json('login'))
