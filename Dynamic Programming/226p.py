N, M= map(int, input().split())

coins = []
for i in range(N):
    coins.append(list(map(int, input())))


#와....이걸어떻게생각하지?....미쳐버리네진짜


d = [10001] * (M + 1)

d[0] = 0

for i in range(N):
    for j in range(coins[i], M + 1):
        if d[j - coins[i]] != 10001:
            d[j] = min(d[j] , d[j - coins[i]] + 1)

if d[M] == 10001:
    print(-1)

else:
    print(d[M])