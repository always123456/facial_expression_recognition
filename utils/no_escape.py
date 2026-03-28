def greet():
    name = input("What's your name?")
    print(f"Hello, {name}")


# KeyboardInterrupt异常同样被except捕获
# 使用ctrl + c来引发KeyboardInterrupt异常从而退出程序的做法就不可行了
# while True:
#     try:
#         greet()
#         break
#     except:
#         print("Error caught")

while True:
    try:
        greet()
        break
    except Exception:
        # KeyboardInterrupt异常没有从Exception类继承，except不会捕获KeyboradInterrupt
        print("Error caught")