name = input("Enter tuple :")
name = tuple(name.split(","))

sum = 0
for i in name:
    sum+=int(i)

print(sum)

