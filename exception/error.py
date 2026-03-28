class A(BaseException):
    pass

class B(BaseException):
    pass



# class MyError(Exception):
#     pass

# def foo():
#     class MyError(Exception):
#         pass
#     raise MyError("这里是foo()函数的作用域里")

# try:
#     foo()
# except MyError:
#     print("这里不会执行,捕获的是全局的MyError")
# except Exception as e:
#     print(f"MyError in foo(): {e}")



# class MyError2(Exception):
#     pass

# try:
#     raise Exception("not MyError2")
# except MyError2:
#     print("这里不会执行，抛出的不是MyError2的类或其子类的实例对象")



# class MyError3(Exception):
#     pass

# class MyError_son(MyError3):
#     pass

# try:
#     raise MyError_son("this is MyError_son")
# except Exception:
#     # 可以捕获所有的子类(包括子类的子类)
#     print("这里不会执行对吗")   
#     print("执行了，靠")
# except MyError3 as e:
#     # 可以捕获子类
#     print(f"This is MyError3, the cause is {e}")



# # 同名不同作用域的两个子类继承自两个不同的父类
# def module_a():
#     class YourError(ValueError):
#         pass
#     return YourError

# def module_b():
#     class YourError(TypeError):
#         pass
#     return YourError

# error_a = module_a()
# error_b = module_b()

# print(error_a is error_b)       # False

# # 同名不同作用域的两个子类继承自同一父类
# def test_a():
#     class YourError(Exception):
#         pass
#     return YourError

# def test_b():
#     class YourError(Exception):
#         pass
#     return YourError

# error_a = test_a()
# error_b = test_b()

# print(error_a is error_b)       # False