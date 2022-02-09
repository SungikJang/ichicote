# num = input()
# nums = num.spilt(" ")
# N = int(nums[0])
# M = int(nums[1])
# K = int(nums[2])
# result = 0
# inputnums = []
# while N>0:
#     inputnums.append(int(input()))
#     N -= 1
#
# inputnums.sort()
# countk = 0
# count1 = 0
# m = 0
# sum = 0
# def sum_ing(k,number, sum):
#     while k >0:
#         sum += number
#         k -= 1
#     return sum
#
# while True:
#     m += K
#     countk += 1
#     if m == M | (M-m)<K:
#         left = M-m
#         break
#     m += 1
#     count1 += 1
#     if m == M | (M-m)<K:
#         left = M - m
#         break
# while countk>0:
#     sum = sum_ing(K, inputnums[2], sum)
#     countk -= 1
# while count1 > 0:
#     sum += inputnums[1]
#     count1 -= 1
#
# sum = sum_ing(left, inputnums[2], sum)
#
# print(sum)


# 이상한 망상에 빠져 시간안에 못풀음ㅋㅋㅋㅋmap 쓰면되는걸 잊어먹음.. 머리가 오지게 안돌아가네
# K번 더하는게 몇번인지 중간에 1번씩 두번쨰큰숫자 더하는게 몇번인지 따로구하고 마지막에 남은 숫자가 뭔지 일일이 다구하려다보니 망해버림
N, M, K = map(int, input().split())
inputnums = list(map(int, input().split()))

inputnums.sort()
sum = 0
def sum_ing(k,number, sum):
    while k >0:
        sum += number
        k -= 1
    return sum

while True:
    for i in range(K):
        if M ==0:
            break
        sum += inputnums[N-1]
        M -=1
    if M == 0:
        break
    sum += inputnums[N - 2]
    M -=1
print(sum)