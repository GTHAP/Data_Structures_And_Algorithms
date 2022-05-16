class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class doublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, newData):
        newNode = node(newData)
        newNode.next = self.head
        if self.head is not None:
            self.head.previous = newNode
            self.head = newNode
            newNode.previous = None
        else:
            self.head = newNode
            self.tail = newNode
            newNode.previous = None
            newNode.next = None

    def printLL(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def getLength(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return print(count)

doublyLLObj = doublyLL()
doublyLLObj.addNode(1)
doublyLLObj.addNode(4)
doublyLLObj.addNode(3)
doublyLLObj.addNode(4)
doublyLLObj.addNode(1)
doublyLLObj.printLL()
doublyLLObj.getLength()
