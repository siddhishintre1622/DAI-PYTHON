x = [[5,8,10], [2,0,9],[5,4,2],[2,3,9]]

dict={}

y = x[0]

for i in y:
    for j in range(1,3):
        dict[i]= x[j]

print(dict)    


#using dictionary comprehension
res = {x[0][ele] : x[ele+1] for ele in range(len(x[0]))}
print(res)