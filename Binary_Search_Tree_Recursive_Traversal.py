class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def addNode(self, node):
        if self.value:
            if node < self.value:
                if self.left is None:
                    self.left = BST(node)
                else:
                    self.left.addNode(node)
            elif node > self.value:
                if self.right is None:
                    self.right = BST(node)
                else:
                    self.right.addNode(node)
        else:
            self.value = node
            
root = BST(4)
root.addNode(2)
root.addNode(6)
root.addNode(1)
root.addNode(8)

def preorder(root):
    if root is None:
        return None
    print(root.value)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print(root.value)
    inorder(root.right)
    
def postorder(root):
    if root is None:
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.value)
    
preorder(root)
inorder(root)
postorder(root)
