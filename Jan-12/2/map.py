array = ["Томирис", "Эрик", "Семен", "Имангали", "Алмаз", "Абулхаир", "Аджибала", "Аян"]

"""
first_letters = map(lambda x: x[0], array)
print(list(first_letters))

length = map(len, array)
print(list(length))

user_in = "7, 9, 12, 17"
# user_list = ["7", "9", "12", "17"]
numbers = map(int, user_in.split(', '))
squares = map(lambda x: x**2, numbers)
for x in squares:
    print(x)
# print(tuple(squares))"""


# reversed_res = map(lambda x: x[::-1], array)
# print(list(reversed_res))

#Объект мап экономичнее в плане памяти
roots = map(lambda x: x ** 0.5, range(1, 11))
print(tuple(roots))
roots = [x**0.5 for x in range(1, 11)]