
import math 

user_num = input("Введите диаметр: ")


try: 
    diametr = float(user_num)



except ValueError:
    print("Вы ввели не число!")

else:
    square = 1/4 * diametr**2 * math.pi
    print("Площадь =", square)