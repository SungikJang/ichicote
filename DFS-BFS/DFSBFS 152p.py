from collections import deque

N, M= map(int, input().split())

maze = []
for i in range(N):
    maze.append(list(map(int, input())))
'''
def DFS(maze, x, y, n, m, s):
    visited = [[0]*m]*n
    visited[0][0] = 1
    if x == n-1 and y == m-1:
        return s
    if maze[x+1][y] != 0 and x+1<n:
        if visited[x+1][y] != 0:
            maze[x + 1][y] = s + 1
            DFS(maze, x + 1, y, n, m, s + 1)

    if maze[x][y+1] != 0 and y+1<m:
        if visited[x][y+1]!=0:
            maze[x][y + 1] = s + 1
            DFS(maze, x, y + 1, n, m, s + 1)

    if maze[x - 1][y] != 0 and x - 1 >= 0:
        if visited[x - 1][y]!=0:
            maze[x - 1][y] = s + 1
            DFS(maze, x - 1, y, n, m, s + 1)

    if maze[x][y - 1] != 0 and y - 1 >= 0:
        if visited[x][y - 1]!=0:
            maze[x][y - 1] = s + 1
            DFS(maze, x, y - 1, n, m, s + 1)
'''

def BFS(maze, x, y, n, m):
    dx = [-1,1,0,0]
    dy = [0,0 ,-1,1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if maze[nx][ny]==0:
                continue

            if maze[nx][ny]==1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
    return maze[n-1][m-1]


print(BFS(maze, 0 , 0 , N , M))
# 겁나어렵네...
