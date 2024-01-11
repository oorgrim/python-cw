#match case

def test_get_names():
    assert get_names([3, 5, 1]) == ["три", "пять", "один"]
    assert get_names((4, 0)) == ["четыре", "ноль"]
    assert get_names([]) == []
    assert get_names((5, 13)) == ["пять", ""]
    assert get_names(1,5,3) == ["один, пять, три"]
    print("test ok")
# args - все элементы передавшиеся от фунеции
def get_names(array: list|tuple) -> list: #| - или
    result = []
    for number in array:
        match number:
            case 0: result.append('ноль')
            case 1: result.append('один')
            case 2: result.append('два')
            case 3: result.append('три')
            case 4: result.append('четыре')
            case 5: result.append('пять')
            case 6: result.append('шесть')
            case 7: result.append('семь')
            case 8: result.append('восемь')
            case 9: result.append('девять')
            case _: result.append('')
    return result


def get_names2(*args) -> list: # * означает, что все, что мы впихнем в качестве аргумента, будет запихнуто в массив(список)
    result = []
    for number in args:
        match number:
            case 0: result.append('ноль')
            case 1: result.append('один')
            case 2: result.append('два')
            case 3: result.append('три')
            case 4: result.append('четыре')
            case 5: result.append('пять')
            case 6: result.append('шесть')
            case 7: result.append('семь')
            case 8: result.append('восемь')
            case 9: result.append('девять')
            case _: result.append('')
    return result

test_get_names()
# get_names2()