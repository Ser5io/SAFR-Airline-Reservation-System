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
        pass
    def append(self, data):
        def append(self, data):
        #////This is the new node////
         new_node = Node(data)
        
        # ////If the list is empty, set head and tail to the new node////
        if self.head is None:
            self.head = self.tail = new_node
        else:
            #////Link the new node to the current tail////
            self.tail.next = new_node
            new_node.prev = self.tail
            #////Update the tail to the new node////
            self.tail = new_node
        self.counter += 1  #////Increment the counter////
    def insert(self, data, pos):
        pass
    def search(self, data):
        pass
    def traverse(self):
        pass
    def removeHead(self):
        pass
    def removeTail(self):
        pass
    def removeAtItem(self, data):
        pass
    def clear(self):
        pass
    def removeAll(self, data):
        pass