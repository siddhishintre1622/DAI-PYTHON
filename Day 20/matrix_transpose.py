import numpy as np


#using for loop
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
y= np.array([[0,0,0],[0,0,0],[0,0,0]])
for row in range(len(x)):
    for column in range(len(x[0])):
        y[row][column]=x[column][row]
print(y)


#using list comprehension
res = [x[j][i] for i in range(len(x)) for j in range(len(x[0]))]
print(res)