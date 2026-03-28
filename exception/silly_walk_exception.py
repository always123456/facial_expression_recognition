class SillyWalkException(RuntimeError):
    def __init__(self, message="Someone walked silly"):
        # 提供了一条默认的错误信息，但仍然可以自定义
        super().__init__(message)
    

def walking(str):
    raise SillyWalkException(f"You want to say:{str}, My walk has gotten rather silly")

try:
    str = input("Enter the message you want to add to the Exception: \n")
    walking(str)
except SillyWalkException as e:
    print(e)