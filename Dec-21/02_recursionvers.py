def get_sum_to_num(num):
    if num == 0:
        return 0
    return num + get_sum_to_num(num - 1)

a = get_sum_to_num(5)
print(a)