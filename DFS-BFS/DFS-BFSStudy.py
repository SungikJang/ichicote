#탐색 알고리즘 DFS/BFS
# 탐색 : 많은 양의 데이터중에서 원하는 데이터를 찾는 과정
# 자료구조 : 데이터를 표현하고 관리하고 처리하기 위한 구조
# ** 오버플로 : 수용가능한 데이터가 가득 찼을때 삽인연상을 수행하면발생, 언더플로 : 데이터가 전혀없는데 삭제 연산을 수행하면 발생


# Stack 스택 : 선입후출 First In Last Out
# 첫 번째 칸부터 데이터가 쌓이고 꺼낼때는 가장 마지막에 들어간 데이터 부터 꺼낸다
stack = []
stack.append(5)
stack.append(3)
stack.append(2)
stack.pop()

print(stack) # [ 5, 3 ]
print(stack[::-1])#최상단 원소 부터 출력 [ 3, 5 ]

# Queue 큐 : 선입선출 First In First Out
# 통과하는 느낌으로 생각 먼저오면 먼저나간다

from collections import deque

queue = deque()

queue.append(5)
queue.append(3)
queue.append(2)
queue.popleft()

print(queue) # [5, 3]
queue.reverse()
print(queue)# [3, 5]


# 재귀함수 : 자기 자신을 호출하는 함수
# 종료시점을 꼭 명시해야한다
# 가장 마지막에 호출된 함수가 먼저 수행을 끝내야 그 앞의 함수가 호출되도록 하기위해 스택 자료구조를 사용한다
# 그렇기 때문에 스택 자료구조를 활용하는 많은 문제들은 재귀함수로 간쳔하게 구현가능
# 반복문보다 코드가 훨씬 간결해짐


# 그래프
# 노드와 간선으로 표현되는 구조
# 두가지 표현 방식 :
# 인접행렬 : 2차원 배열로 연결간계 표현

# (1) - 7 - (0) - 5 - (2)
#     |  0  |  1  |  2
#  0  |  0  |  7  |  5
#  1  |  7  |  0  | 무한
#  2  |  5  | 무한 |  0

INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

# 인접리스트 : 리스트로 그래프 연결 관계 표현
# 연결 리스트 자료구조 이용
# 모든 노드에 연결 노드의 정보 저장
# 0 : (1, 7) , (2, 5)
# 1 : (0, 7)
# 2 : (0, 5)

# 인접행렬을 인접리스트에 비해 차지하는 메모리가 적다 그러나 노드간의 연결정보를 읽는 속도는 인접리스트가 더 빠르다

#DFS 깊이 우선 탐색
# 그래프의깊은 부분을 우선적으로 탐색한다
# 스택 자료구조를 이용하며 구체적인 동작은 다음과 같다
# 1, 탐색 시작 노드 탐색하고 방문처리
# 2, 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 인접노드를 스택에 넣고 방문처리. 방문하지않은 인접노드가 없으면 최상단 노드를 꺼낸다
# 3, 위 과정을 반복

#    1 - 2
#   / \   \
#  3   \   7
#  |\   \ / \
#  4 5   8   6

# 시작노드 1 스택에넣고 방문처리 스택 : [1]
# 최상단 노드 1에 방문하지 않은 인접노드 2 3 8 중 작은 2 부터 스택에 넣고 방문처리 [1, 2]
# 최상단 노드 2에 방문하지 않은 인접노드 7 스택에 넣고 방문처리 [1, 2, 7]
# 최상단 노드 7에 방문하지 않은 인접노드 6 8 중 작은 6 스택에 넣고 방문처리 [1, 2, 7, 6]
# 최상단 노드 6에 방문하지 않은 인접노드 없으므로 6 스택에서 꺼낸다 [1, 2, 7]
# 최상단 노드 7에 방문하지 않은 인접노드 8 스택에 넣고 방문처리 [1, 2, 7, 8]
# 최상단 노드 8에 방문하지 않은 인접노드 없으므로 8 스택에서 꺼냄 [1, 2, 7]
# 최상단 노드 7에 방문하지 않은 인접노드 없으므로 7 스택에서 꺼냄 [1, 2]
# 최상단 노드 2에 방문하지 않은 인접노드 없으므로 2 스택에서 꺼냄 [1]
# 최상단 노드 1에 방문하지 않은 인접노드 3 스택에 넣고 방문처리 [1, 3]
# 최상단 노드 3에 방문하지 않은 인접노드 4 5 중 작은 4 스택넣고 방문처리 [1, 3, 4]
# 최상단 노드 4에 방문하지 않은 인접노드 5 스택에 넣고 방문처리 [1, 3, 4, 5]
# 남은 노드중 방문하지 않은 노드 없으므로 모두 꺼낸다 []
# 1 -> 2 -> 7 -> 6 -> 8 -> 3 -> 4 -> 5

def DFS(graph, v, visited):
    visited[v] = True # 현재노드 방문처리
    print(v, end=' ')

    for i in graph[v]: # 현재노드와 인접한 노드중 방문하지 않은 노드 재귀적으로 방문
        if not visited[i]:
            DFS(graph, i, visited)

graph1 = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

DFS(graph1, 1, visited)

print("\n")
# BFS 너비 우선 탑색
# 가까운 노드 부터 우선 탐색한다.

# 큐의 자로구조를 이용하며 과정은 다음과 같다
# 1, 탑색 시작 노드 큐에 넣고 방문처리
# 2, 큐에서 노드 꺼내고 해당 노드 인접오느 큐에 모두 넣고 방문처리
# 3, 위 과정 반복

# 시작 노드 1 큐에 넣고 방문처리 [1]
# 큐에서 노드 1 빼고 노드 1 방문하지 않은 인접노드 2 3 8 모두 큐에 넣고 방문처리 [2, 3, 8]
# 큐에서 노드 2 빼고 노드 2 방문하지 않은 인접노드 7 큐에 넣고 방문처리 [ , 3, 8, 7]
# 큐에서 노드 3 빼고 노드 3 방문하지 않은 인접노드 4 5 큐에 넣고 방문처리 [ , , 8, 7, 4, 5]
# 큐에서 노드 8 빼고 노드 8 방문하지 않은 인접 노드 없으므로 패스  [ , , , 7, 4, 5]
# 큐에서 노드 7 빼고 노드 7 방문하지 않은 인접 노드 6 큐에 넣고 방문처리 [ , , , ,4, 5, 6]
# 방문하지 않은 노드 없으므로 큐에서 모두 빼준다 []
# 1 -> 2 -> 3 -> 8 -> 7 -> 4 -> 5 -> 6


def BFS(graph, s, visited):
    queue = deque([s])
    visited[s] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
visited = [False]*9
BFS(graph1, 1, visited)