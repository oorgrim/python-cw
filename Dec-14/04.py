text  = input("Введите предложение : ")
fragment = input("Введите фрагмент: ")
position = text.find(fragment)
if position == -1:
    print("Не нашлось")
else:
    print("Нашлось по индексу", position)