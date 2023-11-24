users_data1 = input("введите возраст: ")
try:
    age = int(users_data1)
except ValueError:
    print("Введите число!")
else:
    if age < 120:
        print("Принято.")
    elif age < 3 or age > 120:
        print("Введите корректный возраст.")