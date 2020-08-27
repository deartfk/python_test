from core import student


class ManagerStudent():

    def __init__(self):
        self.student_list = []

    def run(self):
        self.stu_load()
        while True:
            self.show_menu()
            menu_num = int(input('请选择：'))
            if menu_num == 1:
                self.stu_add()
            elif menu_num == 2:
                self.stu_del()
            elif menu_num == 3:
                self.stu_update()
            elif menu_num == 4:
                self.stu_search()
            elif menu_num == 5:
                self.stu_show()
            elif menu_num == 6:
                self.stu_save()
            elif menu_num == 7:
                break

    @staticmethod
    def show_menu():
        print('请选择：')
        print('1,添加学生')
        print('2,删除学生')
        print('3,修改学生')
        print('4,查询学生')
        print('5,显示学生')
        print('6,保存学生')
        print('7,退出系统')


    def stu_load(self):
        pass

    def stu_add(self):
        name = input('请输入姓名:')
        age = input('请输入年龄:')
        tel = input('请输入手机:')

        stu = student.Student(name, age, tel)

        self.student_list.append(stu)

        print(stu)
        print(self.student_list)

    def stu_del(self):
        studel = input('请输入要删除的学生姓名：')
        for i in self.student_list:
            if i.name == studel:
                self.student_list.remove(i)
            else:
                print('查无此人')


    def stu_update(self):
        stuupd = input('请输入要修改的学生姓名：')
        for i in self.student_list:
            if i.name == stuupd:
                try:
                    cal = int(input('手机号修改为：'))
                except:
                    print('请输入正确的数字')
                else:
                    i.tel = cal
                print(i)
            else:
                print('查无此人')

    def stu_search(self):
        find = input('请输入要查找的学生姓名：')
        for i in self.student_list:
            if i.name == find:
                print(i)
            else:
                print('查无此人')


    def stu_show(self):
        for i in self.student_list:
            print(i)


    def stu_save(self):
        pass
