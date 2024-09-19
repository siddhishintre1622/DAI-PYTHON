dict = {
    1 : 'siddhi',
    2 : 'omkar'
}

# new_dict={}
# for i in dict:
#     new_dict[dict[i]] = len(dict[i])
# print(new_dict)

new_dict = {dict[i] : len(dict[i] for i in dict)}
print(new_dict)