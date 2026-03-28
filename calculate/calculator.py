import logging
from operator import add, sub, mul, truediv
import sys

logging.basicConfig(filename="./logs/calculator_log.txt", level=logging.INFO)

def calculator(a, b, op):
    a = float(a)
    b = float(b)
    if op == "+":
        return add(a, b)
    elif op == "-":
        return sub(a, b)
    elif op == "*":
        return mul(a, b)
    elif op == "/":
        return truediv(a, b)
    else:
        raise NotImplementedError(f"No operator {op}")
    # NotImplementedError: 任何未实现的自定义方法和函数应该返回NotImplementError
    # NotImplemented: 任何未实现的特殊方法(双下划线方法)应该返回NotImplemented

if __name__ == "__main__":
    print("""CALCULATOR
    Use postfix notation.
    Ctrl + C or Ctrl + D to quit
    """)

    # except负责捕获异常，防止异常中断了程序的进行
    # 而raise刚好相反，负责重新提出异常，从而中断程序的进行
    while True:
        try:
            equation = input("").split()
            result = calculator(*equation)
            print(result)   
        except NotImplementedError as e:
            print("Invalid operator")
            logging.info(e)     # 在日志中以INFO级别记录异常信息NotImplementedError
        except ValueError as e:
            print("Numbers are not the Expected format")
            logging.info(e)
        except TypeError as e:
            print("Wrong number of arguments.Use:")
            logging.info(e)
        except ZeroDivisionError as e:
            print("Cannot divide by zero")
            logging.info(e)
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye.")
            sys.exit(0)
        except Exception as e:  # 按顺序执行except语句，放在最后
            # 捕获任何继承自Exception的异常对象
            logging.exception(e)    # 记录错误信息，级别为ERROR
            raise e     # except捕获后，重新抛出异常，仍然中断程序进行，但先记录日志