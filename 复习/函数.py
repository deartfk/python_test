# 定义
# def 函数名(形参):
#     函数体
# 调用
# 函数名(实参):

def aa(x, y):
    print(x, y)


aa(1, 2)  # 位置参数
aa(y=4, x=9)  # 关键字参数


# *形参 会以元组形式导入
def hanshuming(*vartuple):
    print(vartuple, type(vartuple))


hanshuming('qw', 88, 00, 'sdf')


# **形参会以字典形式导入
def hanshuming1(**vardict):
    print(vardict, type(vardict))


hanshuming1(a='ee', b='ss')
# 如果单独出现星号 * 后的参数必须用关键字传入
# 形参顺序，（位置参数，*args，关键字参数，**args）


# global和nonlocal

a = 100
def func():
    global a  # 加了个global表示不再局部创建这个变量了. ⽽是直接使⽤全局的a
    a = 28
    print(a)

func()
print(a)


b = 10
def func1():
    b = 20

    def func2():
        nonlocal b  # nonlocal 表⽰在局部作⽤域中, 调⽤⽗级命名空间中的变量.
        b = 30
        print(b)

    func2()
    print(b)

func1()


