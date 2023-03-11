import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# main
T = int(input())
for _ in range(T):
    k = int(input())  # 연산의 개수
    sync = [False] * k  # 최대, 최소 힙 동기화를 위한 리스트
    max_heap = []
    min_heap = []
    for i in range(k):
        op, num = input().split()
        num = int(num)
        
        # 최대힙, 최소힙 두 힙에 삽입
        # 동기화를 위해 i 값 추가
        if op == 'I':
            heappush(max_heap, (-num, i))
            heappush(min_heap, (num, i))
            sync[i] = True
        elif op == 'D':
            # 최대값 삭제
            if num == 1:
                # 없는 값은 계속 삭제(동기화)
                while max_heap and not sync[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    sync[max_heap[0][1]] = False
                    heappop(max_heap)
            # 최소값 삭제
            elif num == -1:
                # 없는 값은 계속 삭제(동기화)
                while min_heap and not sync[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    sync[min_heap[0][1]] = False
                    heappop(min_heap)
    # 연산 종료 후 동기화
    while max_heap and not sync[max_heap[0][1]]:
        heappop(max_heap)
    while min_heap and not sync[min_heap[0][1]]:
        heappop(min_heap)

    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
