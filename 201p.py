def cutting(array, size):
    sum = 0
    for i in array:
        if i > size:
            sum += (i - size)

    return sum


def binary_search(array, target, start, end):
    if start> end:
        return None

    mid = (start + end)//2
    if cutting(array, mid)==target:
        return mid
    elif cutting(array, mid) > target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid-1)



N, M= map(int, input().split())

ricecakes = list(map(int, input().split()))
ricecakes.sort()

result = binary_search(ricecakes, M, 0, ricecakes[N-1])

print(result)