from functools import reduce #утилитка

# свертывание по правилу
array = ["Томирис", "Эрик", "Семен", "Имангали", "Алмаз", "Абулхаир", "Аджибала", "Аян", "Эрик"]
numbers = (87, 543, 765, 0, -432, 54, 654, 213, 123540)

#результат - чистый! в редьюсе
sum = reduce(lambda acc, x: acc+x, numbers) #acc - куда накаплпиваюься значеия (аккмулятор) накопитель изначально определтеь первый элемент    результат - ьто, что осталоьс в аккумуляторе  
# print(sum)

# names = reduce(lambda acc, x: acc + ', ' + x, array)

# ЗНАЧЕНИЕ АККУМ4УЛЯТОРА ПО УМОЛЧАНИЮ
names = reduce(lambda acc, x: acc + ', ' + x, array)
# print(names)

names2 = reduce(lambda acc, x: acc + 1 if x[0] == 'А' else acc, array, 0)
# print(names2)

def name_counter(acc, x):
    if x in acc:
        acc[x] += 1
    
    else:
        acc[x] = 1
    return acc
# последовательное применение функции к элементам списка   


# counts = reduce(name_counter, array, {})

# counts = reduce(lambda acc, x: acc[x] if x in acc else 0)
# print(counts)
# names2 = reduce(lambda acc, x: acc[x] += 1, array, {})
# print(names2)



array = ["Томирис", "Эрик", "Семен", "Имангали", "Алмаз", "Абулхаир", "Аджибала", "Аян", "Эрик", "Виталий"]

names = reduce(lambda acc, x: acc + x[0], array, '')
print(names)


lengths = reduce(lambda acc, x: acc + [len(x)], array, [])
print(lengths)

shortest = reduce(lambda acc, x: acc + [x] if len(x) <7 else acc, array, [])
print(shortest)