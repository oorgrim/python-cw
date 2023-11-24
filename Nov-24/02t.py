user_data = input("Введите число: ")
b = 10

try:
    num = int(user_data)
except ValueError:
    print("ERROR!")
else:
    c = b*2 if num % 2 == 0 else b/2
    print(c)