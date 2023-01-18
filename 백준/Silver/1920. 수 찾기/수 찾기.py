# 수 찾기

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
nums_to_compare = list(map(int, input().split()))
nums.sort()  # 정렬 후 이분 탐색

for num in nums_to_compare:
    left, right = 0, N-1
    mid = (left+right) // 2
    searching = True
    while searching:
        if num == nums[mid]:
            print('1')
            searching = False
        if num > nums[mid]:
            left = mid+1
            mid = (left+right) // 2
        elif num < nums[mid]:
            right = mid-1
            mid = (left+right) // 2
        if left > right:
            print('0')
            searching = False
