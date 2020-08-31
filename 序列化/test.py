import json

dic = {'name': 'dlc', 'age': 18, 'tel': '哦结婚后'}

str_dic = json.dumps(dic, ensure_ascii=False)

print(str_dic, type(str_dic))

with open('json联系', 'w') as f:
    json.dump(dic, f)

with open('json联系','r') as f:
    new_dic = json.load(f)

print(new_dic,type(new_dic))