# 反射是什么？
# 用字符串数据类型的变量名，来访问这个变量的值

# hasattr(对象名,'str类型的变量名')
# getattr(对象名,'str类型的变量名')
import sys


def lalal():
    print('lasdjflasjdf')

# 这个方法 表示所有在当前这个python程序中导入的模块
file = sys.modules['__main__']
getattr(file, 'lalal')()

print(sys.modules)