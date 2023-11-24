user_data1 = input(" Введите номер месяца: ")
try:
    month = int(user_data1)
except ValueError:
    print("Должно быть число, введите число!")
else:
    match month:  
        case 1:
            print("Январь")
        case 2:
            print("февраль")
        case 3:
            print("март")
        case 4:
            print("апрель")
        case 5:
            print("май")
        case 6:
            print("июнь")
        case 7:
            print("июль")
        case 8:
            print("август")
        case 9:
            print("сентябрь")
        case 10:
            print("октябрь")
        case 11:
            print("ноябрь")
        case 12:
            print("декабрь")
        case _:
            print("Не знаю такого месяца")
            