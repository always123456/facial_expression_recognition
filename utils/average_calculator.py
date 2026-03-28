class AverageCalculator:
    def __init__(self):
        self.total = 0
        self.count = 0
    
    # 将多个位置参数收集成一个元组tuple
    def __call__(self, *values):
        # 对象可调用
        if values:
            for value in values:
                self.total += float(value)
                self.count += 1
        return self.total / self.count
    
average = AverageCalculator()
values = input("Enter values, separated by spaces: \n").split()

# 多异常处理：
# try:
#     print(f"Average is {average(*values)}")
#     # *values：把列表values里的元素拆包成多个位置参数
#     # values = ["1", "2", "3"] <-> average("1", "2", "3")
# except ZeroDivisionError:
#     # self.count == 0: ERROR
#     print("ERROR:No values provided")
# except (ValueError, UnicodeError):
#     print(f"ERROR: ALL inputs should be numeric")

# 捕获所有异常：尿布反模式，忽略了具体的异常信息，不推荐，与日志搭配时才可以接受
# 见 no_escape.py 文件
# try:
#     print(f"Average is {average(*values)}")
# except:
#     print("An error occured!")