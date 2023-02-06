import sys
sys.stdin = open('input.txt', 'r')


A = [i for i in range(1, 13)]
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())  # 원수 갯수, 합

    # arr에 대한 모든 경우의 수
    cnt = 0  # 조건을 만족하는 부분집합 수
    for i in range(1 << 12):
        # j: arr의 idx
        tmp = []  # 임시 부분집합
        for j in range(12):
            if i & (1 << j):
                tmp.append(A[j])
        if (len(tmp) == N) & (sum(tmp) == K):
            cnt += 1

    print(f'#{tc} {cnt}')
