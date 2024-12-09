from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.counter = 0
        
    def isEmpty(self):
        return self.top == None
    
    def emptyMsg(self):
        print('Empty list....!')
        
    def peek(self):
        if self.isEmpty():
            self.emptyMsg()
        else:
            return self.top.data
        
    def getSize(self):
        return self.counter
    
    def push(self,data):
        newNode = Node(data)
        if self.isEmpty():
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        
        self.counter += 1
        
    def pop(self):
        if self.isEmpty():
            self.emptyMsg()
        else:
            temp = self.top
            tempData = temp.data
            self.top = self.top.next
            self.counter -= 1
            del temp
            return tempData
    def display(self):
        if self.isEmpty():
            self.emptyMsg()
        else:
            temp = self.top
            print('[',end=' ')
            while temp:
                print(temp.data,end=' ')
                temp = temp.next
            print(']')
            
    def clear(self):
        while self.top:
            temp = self.top
            self.top = self.top.next
            del temp
        self.top = None
        self.counter = 0

stack = Stack()
print(stack.getSize())
stack.push(10)
print(stack.getSize())
stack.push(20)
print(stack.getSize())

stack.push(30)
print(stack.getSize())

stack.push(40)
print(stack.getSize())

print(stack.pop())
print(stack.getSize())

print(stack.peek())
stack.display()
print(stack.getSize())

stack.clear()
print(stack.getSize())
stack.display()