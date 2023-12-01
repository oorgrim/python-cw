user_data = input("Ввкжите число: ")
num = int(user_data)
for i in range(num - 1, 1, -1):
    if num % i == 0:
        print(i)