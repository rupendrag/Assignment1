def calculate_sum_recursive(n):
    if n == 0:
        return 0
    else:
        return n + calculate_sum_recursive(n - 1)

result = calculate_sum_recursive(10)
print("Sum of numbers from 0 to 10:",result)