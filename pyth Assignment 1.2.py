user_input = input("Enter a string: ")

result = ""

for index, char in enumerate(user_input):
    if index % 2 == 0:
        result += char

print(f"Characters at even index positions: {result}")