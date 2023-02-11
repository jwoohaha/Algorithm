import sys
sys.stdin = open('input.txt', 'r')



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail = [[1] * N for _ in range(N)]
    num = 2
    row = 0
    col = 0

    for i in range(N-1):
        # 첫 줄
        col += 1
        snail[row][col] = num
        num += 1


    N -= 1

    while N > 0:

        for i in range(N):
            # 아래 방향
            row += 1
            snail[row][col] = num
            num += 1

        for i in range(N):
            # 왼쪽 방향
            col -= 1
            snail[row][col] = num
            num += 1

        N -= 1

        for i in range(N):
            # 위쪽 방향
            row -= 1
            snail[row][col] = num
            num += 1

        for i in range(N):
            # 오른쪽 방향
            col += 1
            snail[row][col] = num
            num += 1


        N -= 1

    print(f'#{tc}')
    for row in snail:
        print(*row)
