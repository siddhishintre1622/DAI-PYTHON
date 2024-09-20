row = int(input("Enter rows :"))
col = int(input("Enter columns: "))

mat = []

for i in range(row):
    rows=[]
    for j in range(col):
        rows.append(int(input("Enter element :")))
    mat.append(rows)

print(mat)

last = []

for rows in range(row):
    last.append(mat[rows][-1])

print(last)

