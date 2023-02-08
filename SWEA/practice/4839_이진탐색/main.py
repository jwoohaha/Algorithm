import sys
sys.stdin = open('input.txt', 'r')



def binary_search_cnt(P, target):
    # P: 책의 페이지 수, target: 찾는 페이지
    left = 1
    right = P
    cnt = 0
    while True:
        mid = int((left + right) / 2)
        cnt += 1
        if mid > target:
            right = mid
        elif mid < target:
            left = mid
        else:
            return cnt

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    if binary_search_cnt(P, Pa) < binary_search_cnt(P, Pb):
        winner = 'A'
    elif binary_search_cnt(P, Pa) > binary_search_cnt(P, Pb):
        winner = 'B'
    else:
        winner = '0'
    print(f'#{tc} {winner}')
