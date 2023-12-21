def get_sum_to(num):
    sum = 0
    for x in range(0, num):
        sum += x
    return sum
result = get_sum_to(7)
print(result)