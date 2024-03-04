class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError()
    def peek(self):
        if not self.is_empty():
            return self.items[-1] 
    def size(self):
        return len(self.items)
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
print(s1.pop())
print(s1.peek())
print()