def five(x):
    if x%5==0:
        return x/5
    else:
        return x

def three(x):
    if x%3==0:
        return x/3
    else:
        return x

def two(x):
    if x%2==0:
        return x/2
    else:
        return x

def minus(x):
    return x -1

X = int(input())
count = 0
# 못품
# 4가지 연산을 적절히 사용해서 1을 만드는 최소한의 횟수를 구하라 인데
# 이해가 안되네
# 아 음?
# 뭔개소리지

d = [0]*100

for i in range(2,X+1):
    d[i] = d[i-1]+1
    if i%2==0:
        d[i] = min(d[i], d[i//2]+1)
        # 숫자가 2로 나누어 지는경우 2로 나누어주는 경우가 더 횟수가 적은 경우라면 그경우를 채택
    if i%3==0:
        d[i] = min(d[i], d[i//3]+1)
        # 숫자가 3로 나누어 지는경우
    if i%5==0:
        d[i] = min(d[i], d[i//5]+1)
        # 숫자가 5로 나누어 지는경우
# 일단 숫자 1을 빼고 횟수 1을 더해준다음 나누어지는 경우에 따라 횟수를 비교하여 나누는 경우가 더 적다면 그경우 채택하는 방식
    print( d[i])
# 괴어렵네
#ㄹㅇ

