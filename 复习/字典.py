# 语法
# dic = {key:value}
dic = {'name': 'hahha', 'age': 19, '性别': '男'}

# 字典的增加
dic['shengao'] = 99
print(dic)
dic.setdefault('体重', 88)  # 如果已有整个key，则不增加
print(dic)

# 字典的删除
del dic['name']
print('******', dic)
dic.pop('age')  # 返回删除元素的value值
print('******', dic)
dic.popitem()  # 随机删一个键值对，返回元组

# 字典的查找
# 通过key找到value
print(dic['性别'])
# 参数是key值，返回value，如果key不存在，返回default
print(dic.get('name', 'default'))

# 字典的遍历
# 直接遍历字典只会返回key
for i in dic:
    print(i)  # i为字典中key的值
# 输出字典中key和value的值
for i in dic:
    print(i, dic[i])

# 字典的修改
# 通过key修改value
dic['name'] = 'goudan'
print(dic)
# 将dic2的值更新到dic中，没有的话直接插入到dic中
dic2 = {'name': 'lbj'}
dic.update(dic2)
print(dic)

# 返回字典中所有key或者value值
dic.keys()
dic.values()

# 返回可遍历的元组
dic.items()
for k, v in dic.items():
    print(k, v)

# 字典的拷贝
dic3 = dic.copy()
print(dic3)

# 创建一个新字典，key值为lst中的元素，每个key对应的value值为a
lst = ['1', '2', '3']
dic4 = dic.fromkeys(lst, 'a')
print(dic4)
