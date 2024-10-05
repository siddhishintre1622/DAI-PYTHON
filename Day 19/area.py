class circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        return 3.14*self.r**2
    
    def peri(self):
        return 2*3.14*self.r 
    
c1 = circle(int(input("Enter radius :")))
print(c1.area())
print(c1.peri())