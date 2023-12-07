num = input("Введите любое число: ")
half_size = len(num)//2
first_half = num[:half_size]
second_half = num[half_size:]
sum = int(first_half) + int(second_half)
print(f"Сумма первой половины числа {first_half} и второй половины {second_half} равна {sum}")