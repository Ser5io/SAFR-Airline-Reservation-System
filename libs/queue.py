from node import Node

class Queue :
    def __init__(self):
        self.head = self.tail = None
        self.counter = 0
        
    def isEmpty(self):
        return self.head == None
    
    def emptyMsg(self):
        print('Empty list....!')
    
    def getFront(self):
        if self.isEmpty():
            self.emptyMsg()
        else:
            return self.head.data
    
    def getSize (self):
        return self.counter
    
    def enqueue(self,data):
        newNode = Node(data)
        
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.counter += 1
    
    def dequeue(self):
        if self.isEmpty():
            self.emptyMsg()
        else:
            temp = self.head
            tempData = temp.data
            if self.getSize == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            del temp
            self.counter -= 1    
            return tempData

    def display(self):
        if self.isEmpty():
            self.emptyMsg()
        else:
            temp = self.head
            print('[',end=' ')
            while temp:
                print(temp.data,end=' ')
                temp = temp.next
            print(']')
    
    def clear(self):
        while self.head:
            temp = self.head
            self.head = self.head.next
            del temp
        self.head = self.tail = None
        self.counter = 0
