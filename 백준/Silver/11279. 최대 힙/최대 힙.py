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
        # 우선 순위를 기준으로 최소 힙이 구성
        heappush(heap, (-x, x))  # 우선 순위, 값
    # 0이면 가장 작은 값 pop
    elif x == 0:
        if not heap:
            print(0)
        else:
            print(heappop(heap)[1])