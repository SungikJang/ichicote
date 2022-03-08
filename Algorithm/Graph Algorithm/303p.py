from collections import deque
import copy


N = int(input())

#classes = []
classes = [[] for i in range(N+1)]
indgree = [0] * (N+1)
time = [0] * (N+1)
'''
        a = list(map(int, input().split()))
        classes.append(a)


for i in range(1, N + 1):
    time[i] += classes[i - 1][0]
    for l in range(1, len(classes[i - 1])-1):
        if i == classes[i-1][l]:
            continue
        time[i] += time[classes[i-1][l]]

for i in range(1,N+1):
    print(time[i])
'''

for i in range(1,N+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indgree[i] += 1
        classes[x].append(i)
print(classes)
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, N+1):
        if indgree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in classes[now]:
            result[i] = max(result[i], result[now] + time[i])
            indgree[i] -= 1
            if indgree[i] == 0:
                q.append(i)

    for i in range(1,N+1):
        print(result[i])

topology_sort()




# 한 10분 정도 오버 해서 풀었다
# 처음에 위상정렬을 사용하려다가 도저히 생각이안나서 그냥 풀었다
# 풀이에는 위상정렬을 사용한것으로 나온다
# 위상정렬로 풀때 시간정보를 갱신하는 부분에서 틀려서 다음으로 넘어가지 못했다
# 선수 강의가 있을때 동시에 들을 수 있는 경우를 생각해내지 못했다
