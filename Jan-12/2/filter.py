# коммерческий код != спортивное программирование
# предикат - фуенкции, возвращающие тру или ФОЛС ISDIGIT - ПРЕДИКАТ
# не баг -  а фича ! 
# код должен быть чистый и легко читаемый
# джуниор функуиця утилитка консольная вопрос - с чнго начать, фиксить 
# миддл - проекты модуль
# сенньор - новые проекты, руководить планирваие на будущее архитектурнле строение, ритектура, тимлид почти что


array = ["Томирис", "Эрик", "Семен", "Имангали", "Алмаз", "Абулхаир", "Аджибала", "Аян"]

longest = filter(lambda x: len(x) > 6, array)
longest = filter(lambda x: x[0] > "Н", array)
print(list(longest))

numbers = (87, 2, 65, 543, -1, 43, 765, 543)  
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))