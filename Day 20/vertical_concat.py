rows = int(input("Enter rows : "))
cols = int(input("Enter columns :"))

mat=[]

for row in range(rows):
    nrow=[]
    for col in range(cols):
        nrow.append(input("Enter element : "))
    mat.append(nrow)

print(mat)

newm=[]
for col in range(cols):
    for row in range(rows):
        newm.append(mat[row][col])
print(newm)

list = []

i=0

while(i<len(newm)-1):
    list.append(newm[i]+newm[i+1])
    i=i+2


print(list)



