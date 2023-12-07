year = input("Введите год: ")
month = input("Введите месяц: ")
day = input("Введите день: ")

# res = f"{day}.{month}.{year}"
words = "% 22f.% 22f.% 42f"
res = words % (year, month, day)
print(res)