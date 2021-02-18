# 백준2606 바이러스

n = int(input())
m = int(input())
graph=[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b]=graph[b][a]=1

v = 1
def dfs(start, visited):
    visited+=[start]
    for c in range(len(graph[start])):
        if graph[start][c]==1 and (c not in visited):
            dfs(c, visited)
    return visited

print(len(dfs(v,[]))-1)
