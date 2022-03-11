from collections import deque

N = int(input())

fear = list(map(int, input().split()))

fear.sort(reverse=True)
groups = []
count = 0
while count < 5:
    group = []
    index = count
    if fear[count] <= (N - count):
        for l in range(fear[count]):
            group.append(fear[index])
            index += 1
    groups.append(group)
    count = index

print(len(groups))