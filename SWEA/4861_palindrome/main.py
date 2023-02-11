import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # N * N 글자판에서 길이 M인 회문 찾기
    N, M = map(int, input().split())
    texts = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N - M + 1):
            # 가로 방향 탐색
            target = texts[i][j:j + M]
            if target == target[::-1]:
                # palindrome?
                ans = target

    for j in range(N):
        for i in range(N - M + 1):
            # 세로 방향 탐색
            target = ''
            for k in range(M):
                target += texts[i + k][j]
            if target == target[::-1]:
                # palindrome?
                ans = target

    print(f'#{tc} {ans}')

