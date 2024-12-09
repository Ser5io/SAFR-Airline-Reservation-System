from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.counter = 0
        
    # Check if the list is Empty or not
    def isEmpty(self):
        return self.top == None
    
    # Print "Empty list"
    def emptyMsg(self):
        print('Empty list....!')
    
    # Return peek(top)
    def peek(self):
        if self.isEmpty():
            self.emptyMsg()
        else:
            return self.top.data
        
    # Return the size of the stack
    def getSize(self):
        return self.counter
    
    # Add to the top of the stack
    def push(self,data):
        newNode = Node(data)
        if self.isEmpty():
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        
        self.counter += 1
        
    # Remove the top of the stack and return its value 
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
        
    # Print all stack elements
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
            
    # Clear the stack 
    def clear(self):
        while self.top:
            temp = self.top
            self.top = self.top.next
            del temp
        self.top = None
        self.counter = 0