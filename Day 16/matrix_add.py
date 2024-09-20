import numpy as np

a = np.array([[1,1],[2,2]])
b = np.array([[1,1],[2,2]])

#using inbuilt method
# res = np.add(a,b)
# print(res)

#using forloop

for i in range (len(a)):
    for j in range(len(a[0])):
        a[i][j] = a[i][j]+b[i][j]


print(a)



