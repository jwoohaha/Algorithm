import sys
sys.setrecursionlimit(10000)


def dfs(i, j):
    # 배추가 아니면 종료
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
        return
    grid[i][j] = 0
    # 동서남북 탐색
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)



T = int(input())
for tc in range(1, T+1):
    # 가로, 세로, 배추가 있는 위치
    M, N, K = map(int, input().split())
    # 배추 밭 세팅
    grid = [[0] * M for _ in range(N)]
    for _ in range(K):
        m, n = map(int, input().split())
        grid[n][m] = 1

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i, j)
                # 모든 배추 탐색 후 카운트 1 증가
                count += 1
    print(count)
