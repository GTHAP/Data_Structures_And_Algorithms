# A deque is a combination of a stack and queue. Items can be inserted and
# removed from the front and the back of a deque. 
# A list can be used as an underlying data structure.
# Insertion into the front of a deque runs in O(n) or linear time since 
# inserting a new element leads to other elements getting pushed either to 
# the right side. 
# Insertion into the back of a deque runs in O(1) or constant time.
# The 'removefront' method removes an item from the front of the deque.
# The runtime is O(n) since removing from the front leads all the 
# elements in the list moving to the left side.
# The 'removerear' method removes items from the back of the deque.
# The runtime is O(1). 
# The 'peekfront' and 'peekrear' methods allow us to look at the first
# and the last elements in the deque respectively. 
# Both these methods run in constant time - O(1)
# The 'size' and 'isempty' function both run in constant time.

class deque:

    def __init__(self):

        self.items = []

    def addfront(self, item):
        
        self.items.insert(0, item)

    def addrear(self, item):
        
        self.items.append(item)

    def removefront(self):
        
        if self.items: 
          return self.items.pop(0)

        return None

    def removerear(self):
        
        if self.items:
            return self.items.pop()

        return None

    def peekfront(self):
        
        if self.items:
            return self.items[0]

        return None

    def peekrear(self):
        
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        
        if self.items:
            return len(self.items)

        return None

    def isempty(self):
        
        if self.items:
            return self.items == []

        return None
