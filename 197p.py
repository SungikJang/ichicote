# 이진탐색 함수
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


N = int(input())

nums = list(map(int, input().split()))
nums.sort()

M = int(input())

nums_for_check = list(map(int, input().split()))

for num in nums_for_check:
    check = binary_search(nums, num, 0, N - 1)
    if check != None:
        print("yes")
    else:
        print("No")
