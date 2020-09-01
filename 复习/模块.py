# 模块
# 什么是模块
    # 有的功能开发者自己无法完成,这样的话需要借助已经实现的函数\类来完成这些功能
    # 别人写好的一组功能  文件夹/py文件/C语言编译好的一些编译文件
# 语法:
# import 模块名
# from .. import ..


import hashlib

username = 'deartfk'
passwd = '123456'
md = hashlib.md5('deartfk'.encode('utf8'))  # 可以改成动态加盐
md.update(passwd.encode('utf-8'))
print(md.hexdigest())

import logging