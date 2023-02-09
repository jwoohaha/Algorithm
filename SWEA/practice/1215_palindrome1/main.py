import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


T = 10
for tc in range(1, T + 1):
    # 8 * 8 글자판에서 길이 N인 회문 찾기
    N = int(input())
    texts = [input() for _ in range(8)]
    cnt = 0

    for i in range(8):
        for j in range(8 - N + 1):
            # 가로 방향 탐색
            target = texts[i][j:j + N]
            if target == target[::-1]:
                # palindrome?
                cnt += 1

    for j in range(8):
        for i in range(8 - N + 1):
            # 세로 방향 탐색
            target = ''
            for k in range(N):
                target += texts[i + k][j]
            if target == target[::-1]:
                # palindrome?
                cnt += 1

    print(f'#{tc} {cnt}')
