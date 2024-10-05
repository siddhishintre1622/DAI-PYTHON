def add(a,b):
    z = ((a+b)/(a-b))
    return z


try:
    print(add(2,3))
    print(add(3,4))
except:
    print("Error occurred")
else:
    print("Else executed")

finally:
    print("Finally executed")