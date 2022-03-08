N, M = map(int, input().split())

cals = []

parent = [0]*(N+1)
for i in range(N+1):
    parent[i] = i

for _ in range(M):
    a, b, c = map(int, input().split())
    cals.append((a, b, c))

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

for cal in cals:
    c, S1, S2 = cal
    if c == 0:
        union_parent(parent, S1, S2)
    if c == 1:
        a = find_parent(parent, S1)
        b = find_parent(parent, S2)
        if a==b:
            print('Yes')
        else:
            print('No')

# 시간안에 풀었고
# 풀이또한 거의 똑같다
