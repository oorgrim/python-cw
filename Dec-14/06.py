text  = input("Введите предложение : ")
if text.isalpha():
    print("Там только буквы")
elif text.isdecimal():
    print("Там только цифры")
else:
    print("ТАм все что угодно!")