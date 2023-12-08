first_list = [3, 8, 9, 4, 5, 1]  
second_list = [4, 7, 9, 5, 4, 11]
res = []
for elem in first_list:
    if elem in second_list:
        res.append(elem)
if res:
    print("Совпадающие элементы: ", res)
else:
    print('Таковых нет')