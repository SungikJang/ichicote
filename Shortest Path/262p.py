import heapq
INF = int(1e9)


N, M , C = map(int, input().split())

graph = [[] for i in range(N+1)]


for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def improved_dijkstra(start):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


result = improved_dijkstra(C)
print(result)
count = 0
for i in range(len(result)):
    if result[i] >= INF or result[i] == 0:
        result[i] = 0
        continue
    else:
        count += 1

print(str(count) + " " + str(max(result)))

##60 분짜리문제였고 22분 걸렸음

## 최대 거리가 곧 총 걸린 시간인데
## 최대 거리 구할때 좀 더 간단하게 할수 있다는 걸 알게됨 사실 알고 있던건데 문제풀때 생각이안남
## 이번에 안난거 알았고 한번더 보고 넘어가니까 다음엔 기억 날것임
## 그것을 제외하면 풀이와 동일하게 풀었음