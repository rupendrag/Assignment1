def square(x):
    return x**2

l1 = input("Enter the elements of list seperated by space:")
l1 = l1.replace(",", "")
sample_list = l1.split()
sample_list = [int(i) for i in sample_list]

result = list(map(square,sample_list))
print("Original list is: ",sample_list)
print("square list is: ",result)