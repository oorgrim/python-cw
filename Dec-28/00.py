
# test driving development
def sum2(num1, num2):
    return num1 + num2
def test_sum2():
    assert sum2(4, 7) == 11
    assert sum2(-5, 5) == 0
    # assert sum2(7) == 7
    print("Тест пройден")

test_sum2()