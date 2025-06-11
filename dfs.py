def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

graph = {}
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

print("Enter edges (u v):")
for _ in range(e):
    u, v = input().split()
    
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    
    graph[u].append(v)
    graph[v].append(u)  # comment this line for directed graphs

start_node = input("Enter start node: ")

print("\nDFS traversal:")
dfs(graph, start_node)
