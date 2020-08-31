# 定义
# class 类名():
#     属性名 = 123
#
#     def 类方法名(self):
#         pass

class Person:
    # 初始化函数
    def __init__(self,name,age):
        # 初始化属性
        self.name = name
        self.age = age

    def putongfangfa(self):
        print('这是一个普通方法')
        print(self.name,self.age)

    # 静态方法。一般静态方法不需要传参
    @staticmethod
    def printinfo():
        print('这是一个静态方法')

    # 类方法：通过类名调用的方法,类方法中第一个参数约定俗称cls,python自动将类名(类空间)传给cls.
    # 应用场景:
    # 类中 有些方法是不需要对象参与
    # 2, 对类中的静态变量进行改变,要用类方法
    # 3,继承中,父类得到子类的类空间
    @classmethod
    def fun1(cls):
        return cls.name + str(cls.count + 1)


# 实例化一个类
per = Person('dlc',20)  # 如果有初始化参数，必须在实例化时传入
# 调用这个类的方法
per.putongfangfa()

# 创建一个子类
class Son(Person):
    pass

son = Son('shuaishuai',11)
son.putongfangfa()


