the_list = [4, 5, 7, 9, 8]
max_num = max(the_list)
min_num = min(the_list)

changed_first = the_list.index(max_num)
changed_second = the_list.index(min_num)

difference = (changed_first - changed_second)-1
print(difference)
# print(changed_first)
# print(changed_second)