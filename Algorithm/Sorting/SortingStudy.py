# Sorting 정렬
# 데이터를 특정한 기준에 따라 순서대로 나열하는 것



# 선택정렬
# 가장 원시적인 방법
# 가장 작은 원소를 선택하여 자리를 바꾼다

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for l in range(i + 1, len(array)):
        if array[min_index] > array[l]:
            min_index = l
    array[i], array[min_index] = array[min_index], array[i] ## 파이썬의 스와프 코드

# 선택정렬 시간복잡도 : 매번 N-1번 만큼 작은 수를 찾는다. 따라서 N(N + 1)/2 인데 간단히 O(N^2)라고 표현할 수 있다.

# 삽입 정렬
# 데이터를 하나씩 확인하며 각 데이터를 적절한 위치에 삽입한다.
# 선택정렬에 비해 시간적인 측면에서 효율적이다
# 첫 번째 데이터는 그자체로 정렬이 되어있다고 판단하고
# 두번째 데이터 부터 앞선 데이터와 비교하여 적절한위치에 삽입한다
# 이때 앞선 데이터와 비교할때 현재 데이터보다 작은 데이터가 나온다면 그뒤에 삽입하면 된다
# 앞선 데이터들은 이미 정렬이 되어있기 때문이다
# 따라서 거의 정렬 되어 있을수록  더욱 빠르게 동작한다

# 삽입 정렬의 시간복잡도 : 매번 최대 N - 1번 만큼 위치를 옮기기 때문에
# 최대 O(N^2)의 시간복잡도를 갖지만 거의 정렬이 되어있다면 최선의 경우 O(N)의 시간복잡도를 갖게 된다


# 퀵정렬
# 피벗 기준이 되는 데이터를 설정하고 왼쪽에서부터 피벗보다 큰 숫자 오른쪽에서 부터 피벗보다 작은 숫자를
# 찾아 두 숫자를 스왑한다
# 위 과정을 진행하다가 왼쪽에서 부터의 탐색과 오른쪽에서 부터의 탐색이 엇갈릴때 작은 데이터와 피벗을 스왑한다
# 이렇게 되면 피벗은 자신보다 작은 데이터와 큰데이터 가운데 위치하게 된다
# 피벗을 기준으로 파티션 혹은 분할이 발생 하는데 이때 각 분할을 개별로 위 과정을 실행한다
# 과정이 진행됨에 따라 모든 정렬이 이루어질 것이다.

# 스스로 해보기

array = [5,7,9,0,3,1,6,2,4,8]

def Qsort(array, start, end):
    if start == end:
        return
    pivot = start
    Lindex = start + 1
    Rindex = end
    while True:
        for i in range(start+1, end):
            if array[i] > array[pivot]:
                Lindex = i
                break
        for l in range(end, start, -1):
            if array[l] < array[pivot]:
                Rindex = l
                break
        if Rindex <= Lindex:
            break
        array[Lindex], array[Rindex] = array[Rindex], array[Lindex]
        if Rindex == end:
            return
    array[start], array[Rindex] = array[Rindex], array[start]
    if Lindex == Rindex:
        return
    Qsort(array, start, Rindex-1)
    Qsort(array, Lindex, end)

Qsort(array, 0, len(array)-1)

print(array)

#된당...후후하하핳허핳ㅎ
# 안되네..?? 7이랑 8이 왜안바껴?
array = [5,7,9,0,3,1,6,2,4,8]
#퀵 정렬 소스코드
def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right -1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0 , len(array)-1)
print(array)

# 파이썬의 장점을 살린 퀵 정렬

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort1(array):
    if len(array) <=1:
        return array

    pivot  =array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort1(left_side) + [pivot] + quick_sort1(right_side)

print(quick_sort1(array))


# 퀵 정렬의 시간 복잡도
# O(NlogN)이다
# 이미 정렬되어 있는경우 왼쪽을 피벗으로 시작하는 퀵 정렬은 느리게 동작한다
# 반면 데이터가 무작위인 경우 빠르게 작동할 확률이 높다


# 계수정렬
# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘 이다
# 모든 데이터가 양수 일때 계수정렬은 최악의 상황이여도 O(N + K)로 매우 빠른 수행시간을 보장한다
# 다만 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능하다

# 스스로 해보기

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

def CountSort(array):
    nlist = [0] * (max(array)+1)
    newarray = []
    for i in range(max(array)+1):
        for l in array:
            if i == l:
                nlist[i] += 1

    for i in range(len(nlist)):
        for j in range(nlist[i]):
            newarray.append(i)

    return newarray

print(CountSort(array))

# 숫자의 갯수들을 파악하는 부분에서 훨씬 더 간단하게 할 수 있다.
# 책의 코드가 훨 간결하다 하지만 아이디어 자체는 유사하다


# 계수 정렬 코드

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

def count_sort(array):
    newarray = []
    count = [0]*(max(array)+1)

    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            newarray.append(i)

    return newarray

print(count_sort(array))

# 계수 정렬의 공간 복잡도 O(N+K)
# 때에 따라 심각한 비효율성을 초래할 수 있다.
# 예를 들어 데이터가 0과 999,999두개만 존재하더라도 리스트의 크기는 100만이 된다
# 동일한 데이터가 여러개 등장할때 적합한 알고리즘이다
# 데이터의 크기가 한정되고 데이터의 크기가 많이 중복되어 있을수록 유리하며 항상 사용할 수 없다

# 파이썬 정렬 라이브러리
array = [5,7,9,0,3,1,6,2,4,8]

result = sorted(array)
array.sort()

# key를 입력 받을 수 있다
# Lambda도 사용가능

array = [('바나나',2),('사과',5),('당근',3)]
'''
def setting(data):
    return data[1]

result = sorted(array, key=setting)
array.sort(array, key=setting)

print(result)
print(array)
'''

# 정렬 라이브러리의 시간 복잡도
# 최아그이 경우에도 O(NLogN)을 보장한다

#테스트에 사용되는 알고리즘
# 1. 정렬 라이브러리로 풀수 있는 문제
# 2. 정렬 알고리즘의 원리를 물어보는 문제
# 3. 더 빠른 정렬이 필요한 문제

