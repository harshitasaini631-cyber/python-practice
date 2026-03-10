class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
        print(item,"append")    

    def display(self):
        print(self.stack)    


s = Stack()
s.push(10)       
s.push(20)       
s.push(30)   

s.display()
