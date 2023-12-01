user_data = input("Введите число: ")
num = int(user_data)
for i in range(1, 101):
    if i % num == 0:
        print(i)