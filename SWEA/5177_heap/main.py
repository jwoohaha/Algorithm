import sys
sys.stdin = open('input.txt', 'r')


# 재귀로 풀기
def insert_heap(heap, x):
    # heap에 x를 삽입 후 스며오르기
    heap.append(x)
    percolate_up(heap, len(heap)-1)


def percolate_up(heap, i:int):
    # 부모 노드와 재귀적으로 비교하며 작은 값을 루트 노드 쪽으로 올려 보냄
    parent = (i-1) // 2
    if i > 0 and heap[i] < heap[parent]:
        heap[i], heap[parent] = heap[parent], heap[i]
        percolate_up(heap, parent)


T = int(input())
for tc in range(1, T+1):
    # 갯수, 힙에 들어갈 수 리스트
    N = int(input())
    nums = list(map(int, input().split()))
    heap = []
    for num in nums:
        insert_heap(heap, num)
    # 마지막 노드의 조상 노드들의 합
    result = 0
    N -= 1
    while N > 0:
        N = (N-1) // 2
        result += heap[N]
    print(f'#{tc} {result}')


# # 반복으로 풀기
# T = int(input())
# for tc in range(1, T+1):
#     # 갯수, 힙에 들어갈 수 리스트
#     N = int(input())
#     nums = list(map(int, input().split()))
#     nums.insert(0, 0)
#
#     exchange = True
#     while exchange:
#         for i in range(1, N//2+1):
#             exchange = False
#             if (i*2 <= N) and (nums[i] > nums[i*2]):
#                 nums[i], nums[i*2] = nums[i*2], nums[i]
#                 exchange = True
#                 break
#             elif (i*2+1 <= N) and (nums[i] > nums[i*2+1]):
#                 nums[i], nums[i*2+1] = nums[i*2+1], nums[i]
#                 exchange = True
#                 break
#
#     # 마지막 노드의 조상 노드들의 합
#     result = 0
#     while N != 0:
#         N //= 2
#         result += nums[N]
#
#     print(f'#{tc} {result}')
