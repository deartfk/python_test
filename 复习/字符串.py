# 字符串是不可改变的

# str[开始位置:结束位置:步长]
str = 'qwerasfdxzvc'
s = 'qweasdfzxc'
str1 = str[6:2:-1]
print(str[1:2:-1])
print(s[0:-1])
# 按照‘/’字符分割，返回分割后的列表
str.split('/')

# 不传参：去除字符串两边空格；有传参：就去掉字符串两边的参数
str.strip()

# 把传入的字符串以str连接,
# print('_'.join(str))
# print('_'.join(list))

# 字符串大小写
str.upper()
str.lower()
# 将第一个字母转换成大写
str.capitalize()
# 将每个单词第一个字母转换成大写
str.title()

# 字符串中0~8的位置中，a的个数,返回个数
o = str.count('a', 0, 8)
print(o)

# 查找a在字符串0~8中是否存在，存在返回索引，不存在返回-1
print(str.find('a',0,2))
# 查找a在字符串0~8中是否存在，存在返回索引，不存在报错
print(str.index('a',0,8))

# 字符串中的a替换成***
print(str.replace('a','***'))

# 检查字符串在0~2范围内是否以q开头
print(str.startswith('q',0,2))

# str中每个索引的值以@@连接，返回新字符串
'@@'.join(str)

# 格式化字符串
name = 'jaja'
age = 12
print(f'你的名字叫{name},年龄{age}')