dict = {}
dict_n={}

for i in range(5):
    key = input("Enter key : ")
    val = input("Enter value : ")
    dict[key] = val

dict['1']=dict['8']
for v,k in dict.items():
    dict_n[k] = v

print(dict)
print(dict_n)