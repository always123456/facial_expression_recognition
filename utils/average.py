def average(number_string):
    total = 0
    values = 0
    skip = 0

    for n in number_string.split():
        values += 1
        try:
            total += float(n)
        except ValueError:
            skip += 1 # 记录float()失败的跳过次数
    
    if skip == values:
        raise ValueError("No valid numbers provided")
    elif skip:
        print(f"Skipped {skip} invalid values")

    return total / values

if __name__ == "__main__":
    # 重复执行输入 -> 输出，可按ctrl + c引出KeyboardInterrupt异常来退出程序
    while True:
        try:
            line = input("Enter numbers(separated by space):\n")
            avg = average(line)
            print(avg)  
        except ValueError:
            print("No valid numbers provided")