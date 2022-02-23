
garage = int(input())
foods = list(map(int, input().split()))
d = [0] * 100
for i in range(0, garage):
    farray = list(foods)
    if i == 0:
        farray[i] = 0
        farray[i + 1] = 0
    if i == garage-1:
        farray[i - 1] = 0
        farray[i] = 0
    else:
        farray[i - 1] = 0
        farray[i + 1] = 0
        farray[i] = 0
    d[i] = foods[i] + max(farray)

print(max(d))

#맞았는데 완전그냥 내쪼대로 풀어버림ㅋ 공부하는내용과 상관없이 걍품
#하나 배워감 배열을 똑같은 거 하나 더만들때 그냥 ~ = ~하면 안됌!
# 실제풀이 :

d1 = [0]*100
d1[0] = foods[0]
d1[1] = max(foods[0], foods[1])
for i in range(2, garage):
    d1[i] = max(d1[i - 1], d1[i - 2] + foods[i])

# 뭔소린지 모르겠음
# 나는 모든 경우의 수를 구했다. 털기로 마음 먹은 하나의 창고에 따라 발생하는 모든 경우의수를 배열 d에 담아서
# 모든 경우중 가장 큰 것을 채택하는 방식을 사용했다.
#