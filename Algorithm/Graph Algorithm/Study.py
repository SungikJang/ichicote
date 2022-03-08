# Graph Algorithm
# 크루스칼 알고리즘 : 그리디 알고리즘으로 분류
# 위상 정렬 알고리즘 : 큐 자료구조 혹은 스택자료구조로 구현 가능


# 서로소 집합 자료구조
# 공통 원소가 없는 두 집합
# 서로소 부분집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# union과 find 두가지 연산으로 조작할 수 있다.

# 1. union연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다  {
#    1) A 와 B의 루트 노드 A',B'를 각가 찾는다
#    2) A'를 B'의 부모노드로 설정한다(B'가 A'를 가리키도록 한다)
#  }
# 2. 모든 union 연산을 처리할때까지 1.과정을 반복한다.

# 기본적인 서로소 알고리즘 소스코드
'''
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x
이 방식으로 하면 최악의 경우 find함수가 모든 노드를 확인하는 터라 O(N)의 시간복잡도가 걸린다
그 경우 노드의 개수가 V이고 find혹은 union연산의 개수가 M일때 전체 시간 복잡도는 O(VM)이 되어 비효율적이다
하지만 find 함수를 재귀적으로 호출하여 부모 테이블값을 갱신하는 경로압축기법을 통해 최적화 가능하다
경로 압축을 통해 최대 V-1개의 union연산과 M개의 find연산이 가능할때 시간복잡도는 O(V+M(1+log[2-M/V](V)))이다
'''
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] =  find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())

parent = [0]*(v+1)

for i in range(v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합 : ", end='')
for i in range(1,v+1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블 : ', end='')
for i in range(1,v+1):
    print(parent[i], end=' ')



# 서로소 집합을 활용한 사이클 판별  (무방향 그래프내에서의 사이클을 판별할 수 있다)
# 1, 각 산선을 확인하며 두 노드의 루트 노드를 확인한다.
#    1) 루트 노드가 서로 다르다면 두 노드에 대하여 union연산 수행
#    2) 루트 노드가 서로 같다면 사이클이 발생한것이다
# 2, 그래프에 포함된 모든 간선에 대하여 1번과정 반복

# 소스코드

def find_child(parent,x):
    if parent[x] != x:
        parent[x] = find_child(parent, parent[x])
    return parent[x]

# def union_parent() - 위에 있음

v, e = map(int, input().split())

parent = [0]*(v+1)

for i in range(v+1):
    parent[i] = i

Cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        Cycle = True
    else:
        union_parent(parent, a, b)

if Cycle:
    print("사이클이 발생했습니다")

else:
    print("사이클이 발생하지 않았습니다")




# 신장 트리
# 하나의 그래프가 있을때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프


# 최소 신장 트리 알고리즘
# 최소한의 비용으로 신장 트리를 찾아야 하는 경우


# 크루스칼 알고리즘
# 모든 간선에 대해 정렬을 수행한뒤 가장 거리가 짧은 간선부터 집합에 포함시킨다
# 이때 사이클이 발생할수 있는 간선은 포함시키지 않는다
# 간선의 갯수가 E개일때 O(ElogE)의 시간복잡도를 가진다


# 1. 간선 데이터를 비용에 따하 정렬
# 2. 간선을 하나씩 확인 하며 현재의 간선이 사이클을 발생시키는지 확인
#     1) 사이클이 발생하지 않는 경우 최소 신장트리에 포함시킨다
#     2) 사이클이 발생하는 경우 포함시키지 않는다
# 3. 모든 간선에 대하여 2번 과정 반복

# 소스코드

# def find_parent()
# def union_parent()  - 이미 위에 있음


v, e = map(int, input().split())

parent = [0]*(v+1)

edges = []
result = 0

for i in range(v+1):
    parent[i] = i

for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


# 위상 정렬
# 방향그래프의 모든 노드를 방향성에 거스르지 안도록 순서대로 나열하는 것
# 위상정렬의 시간 복잡도는 노드와 간선을 모두 확인한다는 측며에서 O(V+E) 이다

# 진입 차수 : 한 노드로 들어오는 간선의 개수

# 1. 진입 차수가 0인 노드를 큐에 넣는다
# 2. 큐가 빌때 까지 다음의 과정 반복
#    1) 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
#    2) 새롭게 집입차수가 0이 된 노드를 큐에 넣는다

# 소스 코드

from collections import deque

v, e = map(int, input().split())

indgree = [0]*(v+1) # 진입 차수

graph = [[]for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indgree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indgree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indgree[i] -= 1
            if indgree[i] == 0:
                q.append(i)

for i in result:
    print(1,end=' ')



