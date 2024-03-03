def remove_characters(input_string, n):
    new_string = input_string[n:]
    return new_string

input_str = input("Enter String ")
index_to_remove = int(input("Enter number of characters to be removed "))
result = remove_characters(input_str, index_to_remove)

print(f"Original String: {input_str}")
print(f"New String after removing first {index_to_remove} characters: {result}")