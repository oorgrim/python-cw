word = input("Введите любое слово: ")
half_size = len(word)//2
left = word[:half_size]
right = word[half_size:]
print(left)
print(right)