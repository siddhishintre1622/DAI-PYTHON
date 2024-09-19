class Stack:
    list = []
    def __init__(self):
        pass

    def push(self,*args):
        Stack.list.append(args)
    
    def pop(self):
        Stack.list.pop()

    def show(self):
        print(Stack.list)

s =Stack()
s.show()
s.push(5)
s.show()
s.pop()
s.push(8,'a',4,5)
s.show()
    

