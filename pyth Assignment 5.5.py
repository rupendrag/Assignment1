given_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique_list = list(set(given_list))

result_tuple = tuple(unique_list)

min_number = min(result_tuple)
max_number = max(result_tuple)

print("Original List with Duplicates:", given_list)
print("Unique List:", unique_list)
print("Resulting Tuple:", result_tuple)
print("Minimum Number:", min_number)
print("Maximum Number:", max_number)