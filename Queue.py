# Queue also uses a list as the underlying data structure.
# Queue is FIFO. items will be added to the front of the list and removed
# from the back of the list.
# We will use the insert function of the list data structure instead of
# the append function.
# The enqueue method takes O(n) i.e. linear time since all the existing
# elements in the list will be moved to the right when a new element is
# added. 
# The dequque method uses the pop function of the list data structure and
# removes the top (front/end) most item in the list.
# The dequeue method takes O(1) time.
# The peek method returns the last element in the queue. The position 
# '-1' in the list will give us the last element in the list. 
# The peek method takes O(1) time.
# The size method returns the size of the queue using the length 
# function on the list
# It runs in O(1) time. 
# The 'is_empty' method returns whether the queue is empty of not.
# It runs in O(1) time.

class queue:

    def __init__(self):

        self.items = []

    def enqueue(self, item):
        
        self.items.insert(0, item)

    def dequeue(self):
        
        if self.items:
            self.items.pop()

        return None

    def peek(self):
        
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        
        if self.items:
            return len(self.items)

    def is_empty(self):

        if self.items:
            return self.items == []
