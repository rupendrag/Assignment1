from array import array

original_array = array('i', [1, 3, 5, 7, 9])

index_to_remove = 2

if 0 <= index_to_remove < len(original_array):
    original_array.pop(index_to_remove)
    print("Original array after removing the item at index", index_to_remove, ":", original_array)
else:
    print("Index is out of bounds. Cannot remove the specified item.")