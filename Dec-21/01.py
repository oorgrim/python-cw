def compare(num1, num2):
    if num1 < num2:
        return -1
    elif num1 > num2:
        return 1
    else:
        return 0



def new_compare(num1, num2):
    # result = 2 * compare(num1, num2)
    # return result

    return  2 * compare(num1, num2)

new_compare2 = lambda num1, num2: 2 / compare(num1, num2) #соорудить на месте функцию, есть ключ (key)

# result = compare(4, 7) + compare(5, 8)
result = new_compare(4, 7) + new_compare(5, 8)
print(result)