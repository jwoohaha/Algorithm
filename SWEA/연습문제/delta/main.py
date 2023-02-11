import sys
sys.stdin = open('input.txt', 'r')



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    sums = 0
    for i in range(N):
        for j in range(N-1):
            sums += abs(matrix[i][j] - matrix[i][j+1])  # 열 간 차이
            sums += abs(matrix[j][i] - matrix[j+1][i])  # 행 간 차이
    sums *= 2
    print(f'#{tc} {sums}')
