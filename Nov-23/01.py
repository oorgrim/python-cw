
# import math 

user_num1 = input("Введите первое число: ")
user_num2 = input("Введите второе число: ")

try: 
    num1, num2 = int(user_num1), int(user_num2)
    division = num1 / num2



except ValueError:
    print("Вы ввели не число!")

except ZeroDivisionError:
    print("На ноль делить нельзя! ")
else:
    print("Резцльтат: ", division)