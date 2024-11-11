class Node:
    def __init__(self, data):
        self.next = self.prev = None
        self.data = data
        
class Linked_list:
    def __init__(self):
        self.head = self.tail = None
        counter = 0
    
    def isEmpty(self):
        pass
    
    def add(self, data):
        newNode = Node(data)
        
        if self.isEmpty():
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
    
    def append(self, data):
        pass
    
    def insert(self, data, pos):
        pass
    
    def search(self, data):
        pass
    
    def traverse(self):
        pass
    
    def removeHead(self):
        if self.isEmpty():
            return
        
        temp = self.head
        self.head = self.head.next
        temp = None
    
    def removeTail(self):
        pass
    
    def removeAtItem(self, data):
        pass
    
    def clear(self):
        pass
    
    def removeAll(self, data):
        pass