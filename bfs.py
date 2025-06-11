from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

graph = {}
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

print("Enter edges (u v):")
for _ in range(e):
    u, v = input().split()
    
    # Convert to int if needed: u, v = int(u), int(v)
    
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    
    graph[u].append(v)
    graph[v].append(u)  # comment this line if the graph is directed

start_node = input("Enter start node: ")

print("\nBFS traversal:")
bfs(graph, start_node)
