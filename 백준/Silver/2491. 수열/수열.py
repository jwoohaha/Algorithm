N = int(input())
nums = list(map(int, input().split()))
dp_asc = [0] * (N+1)
dp_dsc = [0] * (N+1)
for i in range(N-1):
    if nums[i] >= nums[i+1]:
        dp_dsc[i+1] = dp_dsc[i] + 1

    if nums[i] <= nums[i+1]:
        dp_asc[i+1] = dp_asc[i] + 1

print(max(max(dp_dsc), max(dp_asc))+1)