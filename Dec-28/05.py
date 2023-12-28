#отладка программы    

def generate_num_list(array: list=[]) -> list:
    current_list = []
    sum = 0
    for i in range(len(array)):
        for x in range(len(array))
def test_generate_num_list():
    assert generate_num_list([1, 2, 3, 4, 5]) == [1, 3, 6, 10]
    assert generate_num_list([-1, -2, -3, -4]) == [-1, -3, -6, -10]
    assert generate_num_list([]) == []
    assert generate_num_list([1]) == [1]
    assert generate_num_list() == []
    
    print('test proiden')