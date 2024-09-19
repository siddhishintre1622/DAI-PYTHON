
list = list(input("Enter list : ").split(","))

set = set(list)

print(set)

for i in set:
    max =0
    cnt = 0
   
    for j in list:
        if (j==i):
            cnt+=1   
    if max<cnt:
        max = cnt 
    print(i,"=",max)



            
