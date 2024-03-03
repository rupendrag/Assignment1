def find_first_duplicate(arr):
    seen_elements = set()

    for element in arr:
        if element in seen_elements:
            return element
        seen_elements.add(element)

    return -1

# Example usage:
input_array = [3, 7, 2, 8, 4, 3, 1]
result = find_first_duplicate(input_array)
print("First duplicate element:",result)