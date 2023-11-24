cost = 6500
# if cost < 1000: 
#     print("Скидок нет")
# elif cost < 2000:
#     print("Скидка 2%")
# elif cost < 5000:
#     print("Скидка 5%")
# else:
#     print("скидка 10%")

match cost:
    case x if x < 1000:
        print("сикдок нет")
    case x if x < 2000:
        print("скидка 2%")
    case x if x < 5000:
        print("скидка %")
    case _:
        print("скидка 10%")