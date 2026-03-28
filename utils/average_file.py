def average_file(path):
    file = open(path, "r")

    try: 
        numbers = [float(n) for n in file.readlines()]
        # 如果文件不存在，抛出FileNotFoundError异常，目前允许
    except ValueError as e:
        raise ValueError("File contains non-numeric values.") from e
    else:
        try:
            return sum(numbers) / len(numbers)
        except ZeroDivisionError as e:
            raise ValueError("Empty File") from e
    finally:
        print("close file")
        file.close()