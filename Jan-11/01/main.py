# ИМПОРТЫ
# !! переменные тоже можно импортировать

# import geometry
# geo = geometry

import geometry as geo

# from geometry import get_rectangle_square

# from geometry import * 
#звездочка - импортироавть все (ПЛОХОЙ СПОСОБ - модет привести к проблемам с именами (тяжело отлаживать))

# !! добавить в гит игнор все pyc файлы

circ = geo.get_circle_square(5)
print(circ)

square = geo.get_rectangle_square(10)
print(square)