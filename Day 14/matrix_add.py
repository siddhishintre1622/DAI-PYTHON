
X = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
Y = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(len(X)):
    for column in range(len(X[0])):
        result[row][column] = X[row][column]+ Y[row][column]

for r in result:
    print(r)

for r in range(len(X)):
    for c in range(len(X[0])):
        result[r][c] = X[r][c]*Y[r][c]
for r in result:
    print(r)



