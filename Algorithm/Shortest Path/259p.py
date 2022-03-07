INF = int(1e9)

N, M = map(int, input().split())
lines = []
graph = [[INF]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    lines.append([a, b])

for line in lines:
    graph[line[0]][line[1]] = 1
    graph[line[1]][line[0]] = 1

for l in range(1,N+1):
    for j in range(1, N+1):
        if l==j:
            graph[l][j] = 0

for q in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][q] + graph[q][b])


X, K = map(int, input().split())
result = graph[1][K] + graph[K][X]
if result >= INF:
    print(-1)
else:
    print(result)


# 40분짜리 였고 30분걸림
# 진짜 책하나도 안보고 풀었는데 풀이 완전 똑같음
