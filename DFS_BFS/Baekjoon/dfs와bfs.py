#백준1260 dfs와 bfs

from collections import deque
n, m, v= map(int, input().split())
graph=[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b]=graph[b][a]=1

def dfs(start, visited):
    visited+=[start]
    for c in range(len(graph[start])):
        if graph[start][c]==1 and (c not in visited):
            dfs(c, visited)
    return visited

def bfs(start):
    visited=[start]
    queue=deque([start])
    while queue:  
        n=queue.popleft()
        for c in range(len(graph[start])):
            if graph[n][c]==1 and (c not in visited):
                visited.append(c)
                queue.append(c)
    return visited

print(*dfs(v,[]))
print(*bfs(v))
