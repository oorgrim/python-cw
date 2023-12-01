user_data1 = input("Введите минимальное число: ")
user_data2 = input("Введите максиальное число: ")
num1 = int(user_data1)
num2 = int(user_data2)
counter = 1
for i in range(num1, num2):
    if counter % 4 == 0:
        print(i)
    counter += 1 