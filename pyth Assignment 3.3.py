from array import array

original_array = array('i', [1, 3, 5, 7, 9])

new_item = int(input("Enter the new item "))

original_array.insert(1, new_item)

print("Original array with new item inserted before the second element:",original_array)