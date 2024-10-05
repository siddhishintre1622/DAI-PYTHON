string = input("Enter strig ")
index = int(input("Enter index :"))

list= ""
for i in range(len(string)):
    if i==index:
        continue
    else : 
        list+=string[i]
print(list)
