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
    
def preorderIterative(root):
    if root is None:
        return None
    stack = [root]
    nodeList = []
    while stack:
        node = stack.pop()
        if node is not None:
            nodeList.append(node.value)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
    return nodeList
    
def inorderIterative(root):
    if root is None:
        return None
    stack = []
    nodeList = []
    current = root
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            nodeList.append(current.value)
            current = current.right
    return nodeList
    
def postorderIterative(root):
    if root is None:
        return None
    stack = [root]
    nodeList = []
    while stack:
        node = stack.pop()
        nodeList.insert(0, node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return nodeList
    
print(preorderIterative(root))
print(inorderIterative(root))
print(postorderIterative(root))
