users_data1 = input("введите часы: ")
users_data2 = input("введите минуты: ")
users_data3 = input("введите секунды: ")
hours, minutes, seconds = int(users_data1), int(users_data2), int(users_data3)

try:
    hours, minutes, seconds = int(users_data1), int(users_data2), int(users_data3)
except ValueError: 
    print("Введите число!")
else:    
    if hours > 12 or hours < 0:
        print("Неправильно ввдедены часы, введите числа в диапазоне с 0 до 12")

    elif minutes > 60 or minutes < 0 :
        print("Неправильно ввдедены минуты, введите числа в диапазоне с 0 до 60")
    elif seconds > 60 or seconds < 0 :
        print("Неправильно ввдедены секунды, введите числа в диапазоне с 0 до 60")
    else:
        print("Все данные введены верно")