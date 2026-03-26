# 加入__init__.py文件使其成为可导入的包
from data.loader import load_pgg

if __name__ == "__main__":
    print("执行的是main.py")
    load_pgg()
