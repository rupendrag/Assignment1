def count_case(string1):
    upper_count = 0
    lower_count = 0
    
    for i in string1:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
    return upper_count, lower_count

my_string = input("Enter the sentance")
upperCase, lowerCase = count_case(my_string)
print("No. of Upper case characters: ",upperCase)
print("No. of lower case characters" ,lowerCase)