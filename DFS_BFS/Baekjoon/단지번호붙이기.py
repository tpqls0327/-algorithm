# 백준2667 단지번호붙이기 

n = int(input())
graph=[[0]*(n) for _ in range(n)]

for i in range(n):
    line = input()
    for j, b in enumerate(line):
        graph[i][j] = int(b)

# 좌/우/위/아래 
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(graph, cnt, x, y):
    graph[x][y]=0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if graph[nx][ny]==1:
                cnt = dfs(graph, cnt+1, nx, ny)
    return cnt

ans = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            ans.append(dfs(graph, 1, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)
