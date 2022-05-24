edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]

def createAdjacencyList(edges):
    adjacencyTable = {}
    for edge in edges:
        node1, node2 = edge
        if node1 not in adjacencyTable:
            adjacencyTable[node1] = []
        if node2 not in adjacencyTable:
            adjacencyTable[node2] = []
        adjacencyTable[node1].append(node2)
        adjacencyTable[node2].append(node1)
    return adjacencyTable

table = createAdjacencyList(edges)

def DFS(table, source):
    stack = [source]
    visited = []
    result = []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            result.append(current)
        for node in table:
            if node not in visited:
                stack.append(node)
    return result

source = 4
DFS(table, source)
