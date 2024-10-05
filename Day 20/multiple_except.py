def fun(a):
    if a < 4:
        b = a/(a-3)
    return b

try:
    fun(name)
    fun(3)
    
except ZeroDivisionError:
    print("Zero division error occurred and handled")
except NameError:
    print("Name error occurred and handled")