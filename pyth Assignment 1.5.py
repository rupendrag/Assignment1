x = 0
y = int(input("Enter Range of the numbers"))
for i in range (y):
        y = (x*10+1)
        x=y
        y*=(i+1)
        print(y)