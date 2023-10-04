Sample_list = [(2,5), (1,2), (4,4), (2,3), (2,1)]
l2=[]
Final_list=[]
for i in Sample_list:
    s=i[::-1]
    l2.append(s)
l2.sort()
for i in l2:
    s1=i[::-1]
    Final_list.append(s1)
print(Final_list)
