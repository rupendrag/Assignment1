from array import array

def count_occurrences(arr, element):
    return arr.count(element)

original_array = array('i', [1, 3, 5, 7, 9, 11, 5, 3, 5])

specified_element = int(input("Enter the element to find "))

occurrences = count_occurrences(original_array, specified_element)

print(f"Number of occurrences of {specified_element} in the array:{occurrences}")