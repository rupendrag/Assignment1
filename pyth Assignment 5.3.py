list1 = [2, 3, 4, 5, 6, 7, 8]

list2 = [4, 9, 16, 25, 36, 49, 64]

result_set = {(list1[i], list2[i]) for i in range(min(len(list1), len(list2)))}

print("Resulting Set:",result_set)