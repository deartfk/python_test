class Student():
    '''
    定义学生类
    初始化参数有姓名，年龄，电话
    '''
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    def __str__(self):
        '''
        定义str函数，方便打印学生信息
        :return:
        '''
        return f'姓名：{self.name}，年龄：{self.age}，电话：{self.tel}'
