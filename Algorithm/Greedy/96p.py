N, M= map(int, input().split())
num = 0
for i in range(N):
    nums = list(map(int, input().split()))
    nums.sort()
    if nums[0]>num:
        num = nums [0]


print(num)

#개쉬움