import random
# любой итератор можно преобразовать в лист или кортеж

# my_matrix = random_matrix(4, 6)

# numbers = it_of_matrix(random_matrix)

# nums = it_of_matrix(my_matrix)

def random_matrix(rows, cols):
    the_matrix = []
    for r in range(rows):
        # row = [0] * cols
        # matrix.append(row)
        new_row = [ random.randint(-100, 100) for _ in range(cols)]
        the_matrix.append(new_row)
    return the_matrix

# def it_of_matrix(the_matrix(4, 6))
def it_of_matrix(the_matrix):
    rows = len(the_matrix)
    cols = len(the_matrix[0])
    for r in range(rows):
        for c in range(cols):
            yield the_matrix[r][c]

my_matrix = random_matrix(4, 6)
print(my_matrix)
numbers  = it_of_matrix(my_matrix)

for x in numbers:
    print("%# 05d" % x, end=', ')
    # print(x)