class Student():
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    def __str__(self):
        return f'姓名：{self.name}，年龄：{self.age}，电话：{self.tel}'
