import json
import os


def read_json(filename,key):
    # filepath = os.path.dirname(__file__)+os.sep+'Data'+os.sep+filename
    filepath =r'D:\code\PO_test\tools\Data\login_data.json'
    arr = []
    with open(filepath,'r',encoding='utf-8') as f:
        for i in json.load(f).get(key):
            # print(i)
            arr.append(tuple(i.values())[1:])
    return print(arr)

if __name__ == '__main__':
    read_json('login_data.json','login')