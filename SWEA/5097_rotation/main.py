import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


T = int(input())
for tc in range(1, T+1):
    # 숫자의 수, 맨 뒤로 보내는 작업의 수
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    print(f'#{tc} {nums[M%N]}')

