def gen_numbers(max_num):
    for i in range(max_num + 1):
        yield i #generator

numbers = gen_numbers(10)
# print(numbers, type(numbers))

print(next(numbers))
print(next(numbers))
print(next(numbers))
# print(numbers.__next__( ))



# for x in numbers:
#     print(x)


my_list = [x for x in range(30) if x % 2]
# range генератор возвращает итератор по которому можно двигаться  