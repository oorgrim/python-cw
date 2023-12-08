first_list = [3, 8, 9, 4, 5, 1] 
for i in range(1, len(first_list)) :
    num_after = first_list[i]
    num_before = first_list[i-1]
    if num_after > num_before:
        print(num_after)