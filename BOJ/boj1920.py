# 수 찾기
# 주어진 수 안에 어떤 정수가 존재하는지
# 크기가 크므로 이분탐색 안하면 런타임 초과

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
nums_to_compare = list(map(int, input().split()))
nums.sort()  # 정렬 후 이분 탐색

# 이분탐색 진행
# 이분탐색으로 구한 답이 맞는지 유의해야 함
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

# set로 받아 시간을 단축하는 방법
# import sys
#
# N = int(sys.stdin.readline().rstrip())
# A = set(map(int,sys.stdin.readline().rstrip().split()))
# M = int(sys.stdin.readline().rstrip())
# X = list(map(int,sys.stdin.readline().rstrip().split()))
#
# for x in X:
#     if x in A:
#         print(1)
#     else:
#         print(0)
