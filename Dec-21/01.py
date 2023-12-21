def compare(num1, num2):
    if num1 < num2:
        return -1
    elif num1 > num2:
        return 1
    else:
        return 0

result = compare(4, 7)
print(result)