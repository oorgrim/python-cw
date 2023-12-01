respond = input("Введите предложение: ")
counter = 1
for i in respond:
    if counter % 3 == 0:
        print(i)
    counter += 1 