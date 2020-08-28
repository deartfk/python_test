import sys
path = __file__.split('/')[:-2]
base_path = '/'.join(path)
sys.path.append(base_path)
from core import managerSystem

if __name__ == '__main__':

    ms = managerSystem.ManagerStudent()
    ms.run()

