import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


T = int(input())
for tc in range(1, T+1):
    target, pattern = input().split()
    cnt = 0  # target속 pattern의 수
    N = len(target)
    M = len(pattern)

    i = 0
    while i < N-M+1:
        # target에서 pattern을 찾으면 cnt++
        if target[i:i+M] == pattern:
            cnt += 1
            i += M
        else:
            i += 1
    # 답은 target 길이에서 pattern을 찾은 만큼 절약한 부분을 빼줌
    ans = N - (cnt * M) + cnt
    print(f'#{tc} {ans}')
