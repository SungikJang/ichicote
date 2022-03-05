N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
'''
내 풀이 
굳이 계수정렬코드 쓸필요없는듯
def count_sort(array):
    newarray = []
    count = [0]*(max(array)+1)

    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            newarray.append(i)

    return newarray

sortedA = count_sort(A)
sortedB = sorted(count_sort(B), reverse=True)
'''


'''
내풀이
for i in range(K):
    sortedB[i], sortedA[i] = sortedA[i], sortedB[i]
'''
sortedA = sorted(A)
sortedB = sorted(B, reverse=True)
# 고친풀이
for i in range(K):
    if sortedA[i]>sortedB[i]:
        break
    sortedB[i], sortedA[i] = sortedA[i], sortedB[i]

sum = 0
for i in sortedA:
    sum += i
#이것도 그냥 라이브러리 sum(sortedA) 하면 간단하다


print(sum)

#풀이
# 나의 풀이와 아이디어는 똑같지만 그냥 정렬라이브러리를 사용해서 더간단하게 풀이했다
# 그리고 나의 풀이는 A의남은 원소들이 B의 남은 원소들보다 큰 경우를 따지지 않았다

