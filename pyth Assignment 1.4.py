def is_first_and_last_equal(lst):
    if len(lst) < 1:
        return False
    return lst[0] == lst[-1]

# Example usage:
numbers = [1, 2, 3, 4, 1]
result = is_first_and_last_equal(numbers)

print(f"Are the first and last numbers equal{result}")