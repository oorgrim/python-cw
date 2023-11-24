# is 
# isnt
# and
km_to_miles = 1.6
user_data = input("Введите количество километров: ")

try:
    #... здесь программа стала непредсказуемой 
    km = float(user_data)
except ValueError: 
    print("не поолучилось")
else:
    if km >= 0:
        dist = km * km * km_to_miles
        print("Результат:", dist, "миль")
    else:
        print("с отрицаельными не раюотаем")