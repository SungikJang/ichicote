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

N, M = map(int, input().split())

lines = []
parent = [0]*(N+1)
for i in range(N+1):
    parent[i] = i

for _ in range(M):
    a, b, c = map(int, input().split())
    #lines.append((a, b, c))
    lines.append((c,a,b))
'''
def getKey(tup) :
    return tup[2]
lines.sort(key = getKey)
'''
lines.sort()
distance = []
for i in range(len(lines)):
    cost, a, b = lines[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        distance.append(cost)
    else:
        lines[i] = (0,0,0)

result = 0
for i in distance:
    if i != max(distance):
        result += i


print(result)

# 5분 남기고 풀었다
# getkey안쓰고 그냥 처음부터 lines에 append할때 c,a,b로 하면될거같다
# 나머지 과정은 풀이와 거의 똑같다