def list_sum(input_list):
    total = 0
    for i in input_list:
        total+=i
    return total

l1 = input("Enter the elements of list seperated by space:")
l1 = l1.replace(",", "")
my_list = l1.split()
my_list = [int(i) for i in my_list]


result = list_sum(my_list)
print(result)