def reverse_string(input_string):
    reverse_str = ""
    for i in input_string:
        reverse_str=i+reverse_str
    return reverse_str

my_string = input("enter the string")
reverse_str = reverse_string(my_string)
print(reverse_str)