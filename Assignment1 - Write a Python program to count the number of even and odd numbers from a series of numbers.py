# Write a Python program to count the number of even and odd numbers from a series of numbers.

series = (1,2,3,4,5,6,7,8,9)
odd_num = []
even_num = []
for i in series:
    if i%2==0:
        even_num.append(i)
    else:
        odd_num.append(i)
print("Number of even numbers :",len(even_num))
print("Number of odd numbers :",len(odd_num))
