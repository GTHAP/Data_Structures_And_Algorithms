numberOfNodes = 5

edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]

class Graph:
    def __init__(self, numberOfNodes, edges):
        self.numberOfNodes = numberOfNodes
        self.data = [[] for _ in range(numberOfNodes)]
        for node1, node2 in edges:
            self.data[node1].append(node2)
            self.data[node2].append(node1)
    def __repr__(self):
        return "\n".join(["{}: {}".format(node, neighbors) for node, neighbors in enumerate(self.data)])
    def __str__(self):
        return self.__repr__()

graph1 = Graph(numberOfNodes, edges)

def DFS(graph, root):
    stack = [root]
    result = []
    visited = []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            result.append(current)
            for node in graph.data[current]:
                if node not in visited:
                    stack.append(node)
    return result

DFS(graph1, 0)
