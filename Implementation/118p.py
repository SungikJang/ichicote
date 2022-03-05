N, M = map(int, input().split())

visit = [[0]* M for _ in range(N)]

X, Y , Dir = map(int, input().split())

visit[X][Y] = 1

Map = []
for i in range(N):
    Map.append(list(map(int, input().split())))


dirX = [-1,0,1,0]
dirY = [0,1,0,-1]

def turn():
    global Dir
    Dir -= 1
    if Dir == -1:
        Dir = 3


count = 1
turncount = 0

while True:
    turn()
    NX = X + dirX[Dir]
    NY = Y + dirY[Dir]

    if visit[NX][NY] == 0 | Map[NX][NY] == 0:
        visit[NX][NY] = 1
        X = NX
        Y = NY
        count+=1
        turncount = 0
        continue
    else:
        turncount+=1
    if turncount==4:
        NX = X - dirX[Dir]
        NY = Y - dirY[Dir]
        if Map[NX][NY] == 0:
            X = NX
            Y = NY
        else:
            break
        turncount = 0

print(count)