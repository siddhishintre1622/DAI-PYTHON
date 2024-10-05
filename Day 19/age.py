
class Person:
    def __init__(self,n,c,d):
        self.n = n
        self.c = c
        self.d =d
    
    def age(self):
        age = 2024 - self.d
        return age
    
p1 = Person("s","i",2000)
print(p1.age())




        