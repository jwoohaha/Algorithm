from sys import stdin
input = stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
M = int(input())
check_nums = list(map(int, input().split()))

# 이분탐색으로 구현했으나 시간초과
# 딕셔너리로 hash 이용하면 쉽게 해결 가능

hashing = {}
for num in nums:
    if num in hashing:
        hashing[num] += 1
    else:
        hashing[num] = 1

for check_num in check_nums:
    if check_num in hashing:
        print(hashing[check_num], end = ' ')
    else:
        print('0', end = ' ')

# 이분탐색

# def binary_search(n, nums, start, end):
#     if start > end:
#         return 0
#     mid = (start+end)//2
#     # 해당 구간에서 n의 개수를 세서 리턴
#     if n == nums[mid]:
#         return nums[start:end+1].count(n)
#     elif n < nums[mid]:
#         return binary_search(n, nums, start, mid-1)
#     else:
#         return binary_search(n, nums, mid+1, end)
#
# N = int(input())
# nums = list(map(int, input().split()))
# nums.sort()
# M = int(input())
# check_nums = list(map(int, input().split()))
#
# for check_num in check_nums:
#     start = 0
#     end = len(nums) - 1
#     print(binary_search(check_num, nums, start, end), end = ' ')