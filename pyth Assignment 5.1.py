list1 = [3, 6, 9, 12, 15, 18, 21]

list2 = [4, 8, 12, 16, 20, 24, 28]

result_list = [list1[i] for i in range(1, len(list1), 2)] + [list2[i] for i in range(0, len(list2), 2)]

print("Resulting List:",result_list)