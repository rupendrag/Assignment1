previous_number = 0

for i in range(1, 11):
    current_number = i
    total = current_number + previous_number
    print(f"Current: {current_number}, Previous: {previous_number}, Sum: {total}")
    previous_number = current_number