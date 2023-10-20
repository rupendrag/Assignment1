def triple(x):
    return x*3

l1 = input("Enter the elements of list seperated by space:")
l1 = l1.replace(",", "")
my_list = l1.split()
my_list = [int(i) for i in my_list]

result = list(map(triple,my_list))
print("Original List is: ",my_list)
print("triple list is: ",result)