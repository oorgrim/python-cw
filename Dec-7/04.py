film = input("Введите название фильма: ")
cinema = input("Введите название кинотеатра: ")
time = input("Введите время: ")

words = "Билет на %s в %s на %s забронирован."
res = words % (film, cinema, time)
print(res)