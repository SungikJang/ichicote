N = int(input())

LRUD = list(map(str, input().split()))

X = 1
Y = 1
def move_ing(movement, x, y, N):
    if movement == "L":
        if y!=1:
            y += 1
    if movement == "R":
        if y != N:
            y += 1
    if movement == "U":
        if x !=1:
            x += 1
    if movement == "D":
        if x != N:
            x += 1
    return x, y

for move in LRUD:
    result = move_ing(move, X, Y, N)
    X = result[0]
    Y = result[1]


print(result)