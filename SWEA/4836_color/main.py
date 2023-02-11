import sys
sys.stdin = open('input.txt', 'r')



T = int(input())
for tc in range(1, T+1):
    area = [[0]*10 for _ in range(10)]
    cnt = 0
    N = int(input())
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):  # 행
            for j in range(c1, c2+1):  # 열
                area[i][j] += 1

    for i in range(10):
        for j in range(10):
            if area[i][j] == 2:
                cnt += 1

    print(f'#{tc} {cnt}')
