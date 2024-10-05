r = int(input("Enter rows :"))
c = int(input("Enter columns :"))

matrix=[]

for i in range(r):
    rows=[]
    for j in range(c):
        rows.append(int(input()))
    matrix.append(rows)

#print(matrix)

for i in matrix:
    for j in i:
        print(j,end=" ")
    print()

