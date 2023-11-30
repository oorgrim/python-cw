num = ""
while num == "":

    user_data = input("ВВедите число: ")
    try:
        num = int(user_data)
    except ValueError:
        print("Введите число!")
        # exit()
    
while num <= 10:
    print("Число НЕ больше 10")
    num += 1
# else:
#     print("ЧИсло больше 10")\

        




# while i < N:
#     i+=1