# A stack is a data structure based on Last In First Out (LIFO) principal
# In python a list can be used to implement a stack
# A stack will have push and pop methods
# The push method will push an element to the end of the stack and the pop method will pop the element at the end of the stack
# [ 10, 2, 8, 5 ] - This is what the stack will look like after pushing the elements into it

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def max(self):
        sort = sorted(self.stack)
        return print(sort.pop())

    def printstack(self):
        for i in self.stack:
            print(i)

Value = Stack()
Value.push(10)
Value.push(2)
Value.push(8)
Value.push(5)
Value.printstack()
Value.pop()
Value.printstack()
Value.max()
Value.printstack()
