dict = {
    'a' : 100,
    'b' : 200,
    'c' : 300
}

sum = 0

for i in dict:
    sum += dict[i]

print(sum)

print(sum(dict[i] for i in dict))