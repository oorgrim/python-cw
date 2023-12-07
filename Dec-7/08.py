str = input("Введите предложение: ")
for i in str:
    if i % 2 == 1:
        upper = str[i] = i.upper() 
    else:
        lower = str[i] = i.lower()

        # lower = i.lower()
# print(upper, lower)