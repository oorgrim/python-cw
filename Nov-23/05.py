week = input(" Введите день недели: ")

match week:  #match сопоставляет с образцом
    case "вс":
        num = 7
    case "пн":
        num = 1
    case "вт":
        num = 2
    case "ср":
        num = 3
    case "чт":
        num = 4
    case "пт":
        num = 5
    case "сб":
        num = 6
    case _:
        num = 0
print("Номер дня: ", num)