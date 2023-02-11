import sys
sys.stdin = open('input.txt', 'r')



T = 10
for _ in range(1, T+1):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    sums = []
    for i in range(100):
        # 행 합
        sums.append(sum(matrix[i]))

    for j in range(100):
        # 열 합
        col_sum = 0
        for i in range(100):
            col_sum += matrix[i][j]
        sums.append(col_sum)

    diagonal_sum_down = 0
    diagonal_sum_up = 0
    for i in range(100):
        # 대각선 합
        diagonal_sum_down += matrix[i][i]
        diagonal_sum_up += matrix[99-i][i]

    sums.append(diagonal_sum_up)
    sums.append(diagonal_sum_down)

    print(f'#{tc} {max(sums)}')
