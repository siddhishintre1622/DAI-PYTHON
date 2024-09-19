nums = input("Enter tuple :")
nums = list(nums.split(","))


cubelist=[]

for i in nums:
    cube=[]
    cube.append(i)
    cube.append(int(i)**3)
    cubelist.append(tuple(cube))

print(cubelist)