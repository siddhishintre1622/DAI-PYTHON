string = input("enter string :")

print(string)

for i in string:
    if((i>'a' and i<'z' ) or (i>'A' and i<'Z')):
        print(i,end='')
        