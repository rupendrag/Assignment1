d = {}
Integer_value = ord('a')
for i in range(26):
    letter = chr(ord('a')+i)
    d[letter] = Integer_value+i
print(d)