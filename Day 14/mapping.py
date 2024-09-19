
test_list = [{'name': 'Manjeet', 'age': 23},
             {'name': 'Akshat', 'age': 22},
             {'name': 'Nikhil', 'age': 21}]

dict = {}

for i in test_list:
    dict[i['name']]=dict[i['age']]

print(dict)


    