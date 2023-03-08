import sys
input = sys.stdin.readline
from heapq import heappop, heappush



# main
N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    # 자연수라면 추가 연산
    if x > 0:
        heappush(heap, x)
    # 0이면 가장 작은 값 pop
    elif x == 0:
        if not heap:
            print(0)
        else:
            print(heappop(heap))