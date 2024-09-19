n = int(input("Enter number : "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact *i
# print(fact)


def fact(n):
    if n==0:
        return 1
    else :
        return n * fact(n-1)
    
print(fact(n))
    
