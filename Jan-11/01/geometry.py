# вынести функцию в модуль 

import math
def get_circle_square(radius: float) -> float:
    result = math.pi * radius**2
    return result

def get_rectangle_square(a: float, b:float = None) -> float:
    if b is None:
        b = a
    result = a * b
    return result

def test_get_rectangle_square():
    assert get_rectangle_square(10) == 100
    assert get_rectangle_square(10, 3) == 30
    assert get_rectangle_square(10, 0) == 0
    print('тест пройден')
    
def test_get_circle_square():
    # assert get_circle_square(5) == 78.5
    assert get_circle_square(0) == 0
    print('тест пройден2!!! урааа')

test_get_rectangle_square()
test_get_circle_square()