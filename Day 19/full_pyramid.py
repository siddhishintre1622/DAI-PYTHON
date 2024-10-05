n = int(input("Enter no : "))

for i in range(0,n):
    for j in range(1,n-i):
        print(" ",end='')
    for k in range(1,i*2):
        print("*",end='')
    print()