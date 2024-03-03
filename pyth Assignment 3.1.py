from array import array

original_array = array('i', [1, 3, 5, 7, 9])

reversed_array = array('i', reversed(original_array))

reversed_array.append(11)

print("Original array:", original_array)
print("New array:",reversed_array)