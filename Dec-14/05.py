text  = input("Введите предложение : ")
fragment = input("Введите фрагмент: ")

try:
    position = text.index(fragment)
except ValueError:
    print("Не нашлось")
else:
    print("Нашлось", position )