
import math 

user_num1 = input("Введите первое число: ")
user_num2 = input("Введите второе число: ")

try: 
    num1, num2 = int(user_num1), int(user_num2)

except ValueError:
    print("Вы ввели не число!")

else:
    difference = num1 - num2
    try:
        result = math.sqrt(difference)
    except ValueError:
        print("первое число дожно быьт больше второго!")
    else:
        print("Результат =", result)