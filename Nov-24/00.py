
# km_to_miles = 1.6
# user_data = input("Введите количество километров: ")

# try:
#     km = float(user_data)
# except ValueError: 
#     print("не поолучилось")
# else:
#     if km >= 0:
#         dist = km * km * km_to_miles
#         print("Результат:", dist, "миль")
#     else:
#         print("с отрицаельными не раюотаем")


km_to_miles = 1.6
user_data = input("Введите количество километров: ")

try:
    km = float(user_data)
except ValueError: 
    print("не поолучилось")
else:
    if km >= 0:
        dist = km  / km_to_miles
        dist = round(dist, 2) #округлить до второго знака
        print("Результат:", dist, "миль")
    else:
        print("с отрицаельными не раюотаем")