users_data1 = input("введите числo: ")
try:
    num = float(users_data1)
except ValueError:
    print("Введите число!")
else:

    if num > 0:
        print("число положительное")
    elif num >= 0:
        print("число = 0")
    else:
        print("число отрицательное")