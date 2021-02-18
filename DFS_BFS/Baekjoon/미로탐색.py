# 백준2178 미로탐색

from collections import deque

n, m = map(int, input().split())
graph=[[0]*(m) for _ in range(n)]

for i in range(n):
    line = input()
    for j, b in enumerate(line):
        graph[i][j] = int(b)
visited = [[0]*m for _ in range(n)]

# 좌/우/위/아래 
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, cnt = 1):
    graph[x][y] = 0
    while q:
        now_x, now_y, cnt = q.popleft()
        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0 or not graph[nx][ny]:
                continue
            graph[nx][ny] = 0
            q.append((nx, ny, cnt+1))
            if nx == end[0] and ny == end[1]:
                return cnt+1
                break
    return -1

start, end = (0, 0, 1), (n-1, m-1)

q = deque([])
q.append(start)
print(bfs(start[0],start[1],start[2]))
