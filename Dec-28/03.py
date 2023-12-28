user_list = input('Введите числа: ')
input_nums_list = user_list.split()
nums = []
for num_str in input_nums_list:
    try:
        num = int(num_str)
        nums.append(num)
    except:
        print(f'{num_str} не является числом. Пропускаю это значение')
print(f'Ваш список: {nums}')