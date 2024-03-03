given_list = [47, 64, 69, 37, 76, 83, 95, 97]

given_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

for element in given_list[:]:
    if element in given_dict.values():
        given_list.remove(element)

print("Updated List:",given_list)