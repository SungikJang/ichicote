

N, M= map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))


def DFS(graph, x, y, n, m):
    if x<=-1 or x>=n or y<=-1 or y>=m: # 범위를 벗어나는 순간 종료
        return False

    if graph[x][y]==0:
        graph[x][y] = 1
        DFS(graph, x - 1, y, n, m)  # 인접 노드 재귀적으로 호출
        DFS(graph, x + 1, y, n, m)
        DFS(graph, x, y - 1, n, m)
        DFS(graph, x, y + 1, n, m)
        return True
    return False

count = 0
for i in range(N):
    for l in range(M):
        if DFS(graph, i, l, N, M) == True:
            count += 1

print(count)


# 풀이위한 접근은 정답의 풀이방식과 같았는데 구현하지 못했다
# 너무 복잡하게 생각한거같다
# 첫칸부터 인접한 노드들을 확인하면서 진행하려 했는데 첫노드부터 다확인한다는게 잘못된 생각이였던거같다.
# 결국 DFS던 BFS던 활용할 아이디어가 떠오르지 않았다
# 두가지를 좀더 이해하고 활용 많이 해봐야될듯