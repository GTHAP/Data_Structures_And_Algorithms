class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        newNode = Node(value)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        current = self.head
        while(current):
            print(current.value)
            current = current.next

llObject = LinkedList()
llObject.insert(7)
llObject.insert(7)
llObject.insert(3)
llObject.insert(5)
llObject.printLL()
