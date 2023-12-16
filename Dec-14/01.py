
user_data = input("Введите предложение: ")

seek_from = int(input("От скольки до скольки считать: "))
seek_to = int(input("До скольки начать считать: "))
fragment = input("че ищем: ")
result = user_data.count(fragment, seek_from, seek_to)
print(result)