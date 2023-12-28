
def chot(numbers = []) -> list: 
    #если нужна пустая структура, то: 
# def chot(numbers = ()) -> list: 
    
    result = []
    for x in numbers:
        if x % 2 == 0:
            result.append(x)
    return result

def test_chot():
    assert chot([1, 2, 3, 4]) == [2, 4]
    assert chot([1, 7, 3, 11, 27]) == []
    assert chot([]) == []
    assert chot((2, 3, 7, 4, 11)) == [2, 4]
    assert chot() == []
    print('тест пройден')
test_chot()