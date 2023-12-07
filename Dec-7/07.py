str = input("Введите предложение: ")
letter = input("Введите букву: ")

i_first, i_last = -1
for i in range(len(str)):
    symbol = str[i]
    if symbol == letter:
        i_first = symbol
print(i_first)
# print(i)