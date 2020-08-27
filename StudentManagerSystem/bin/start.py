import sys
import os
path = __file__.split('/')[:-2]
base_path = '/'.join(path)
sys.path.append(base_path)
from core import managerSystem
from core import student






if __name__ == '__main__':
    # man_sys = managerSystem.ManagerSudent()
    # man_sys.run()
    # print(managerSystem.ManagerSudent.stu_add())

    ms = managerSystem.ManagerStudent()
    ms.run()
