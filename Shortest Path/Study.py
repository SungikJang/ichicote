# 최단경로
# 최단경로 찾는 알고리즘
# 효율적인 알고리즘이 3가지 다익스트라, 플로이드 워셜, 벨만 포드 알고르짐으로 이미 정립되어있음


# 다익스트라 알고리즘
# 그래프에서 여러개 노드가 있을때 최단경로를 찾는 알고리즘
# 음의 간선이 없을경우 정상작동한다 -> 현실 GPS의 기본 알고리즘
# 그리디 알고리즘으로 분류됨 현재 가장 짧은 경로를 찾는 임의의 과정을 반복한다.

# 출발노드설정
# 최단거리 테이블 초기화
# 방문하지 않은 노드중 최단 거리인 노드 선택
# 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단거리 테이블 경신
# 위 두 과정 반복

# 스스로 짜보기 이취코테 P.233
from collections import deque
INF = int(1e9)

graph = [
    [],
    [(2, 2), (3, 5), (4, 1)],
    [(3, 3), (4, 2)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    []
]

d = [INF] * 7

visited = [False] * 7
visited[0] = True
d[1] = 0


def spf(graph, v, visited, d):
    if visited[v] == True:
        return
    visited[v] = True
    if all(visited):
        return True
    unvisitnode = []
    for i in graph[v]:
        d[i[0]] = min(d[i[0]], d[v] + i[1])
    for a in range(7):
        if not visited[a]:
            unvisitnode.append(d[a])
    index = []
    n = min(unvisitnode)
    for a in range(7):
        if d[a] == n:
            index.append(a)
    for ind in index:
        spf(graph, ind, visited, d)


spf(graph, 1, visited, d)

for i in d[1:]:
    if i == INF:
        print("INFINITY")
    else:
        print(i, end=' ')


# 다익스트라 알고리즘

import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

start = int(input())

graph = [[] for i in range(N+1)]

visited = [False] * (N + 1)

distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,N+1):
        if distance[i]<min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start]= True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(N-1):
        now = get_smallest_node()
        visited[now]=True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, N+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])

print(graph)


# 다익스트라의 시간복잡도
# O(V^2)이다 왜나햐면 총 O(V)번에 걸쳐 최단거리가 짧은 노드를 매번 선형 탑색해야 되고
# 매번 일일히 현재노드와 연결된 노드를 확인하기 때문이다

# 노드의 개수가 5000개이하라면 왠만하면 위의 코드로 풀수 있지만
# 10000개를 넘어간다면 개선된 다익스트라 알고리즘을 사용해야 한다

# 개선된 다익스트라 알고리즘
# 최악의 경우에도 시간복잡도 O(ELogN)을 보장한다  (E:간선의 개수, V:노드의 개수)
# 원래는 선형적으로 찾아서 O(V)의 시간복잡도가 걸리는 최단거리가 짧은 노드찾기를 선형적으로 찾지않고
# 더욱 빠르게 찾는다면 시간복잡도를 줄일 수 있다
# 힙(Heap)을 사용하여 특정노드까지의 최단거리에 대한 정보를 힙에 담아서 처리하므로
# 출발노드로부터 가장 거리가 짧은 노드를 빨리 찾을 수 있다
# 힙은 우선순위 큐를 구현하기위한 자료구조중 하나이다
# 우선순위 큐는 파이썬에서 라이브러리 PriorityQueue오 heapq를 사용할 수 있는데
# 시간이 제한된 상황에선 더 빠른 heapq를 사용하자
# 파이썬의 우선순위큐는 기본적으로 최소힙구조로 되어있음 따라서 최단거리를 구해야하는 다익스트라에선
# 그대로 사용하면된다 또한 최소힙 구조에서 -부호를 사용하여 꺼낼때 다시 음수 부호를  붙여 원래값으로 돌리는 방식으로 최대힙처럼 사용할 수 있다

import heapq

distance = [INF] * (N + 1)
def improved_dijkstra(start):
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

improved_dijkstra(start)
for i in range(1, N+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
