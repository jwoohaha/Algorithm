import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')

# 0: 통로, 1: 벽, 2: 출발, 3: 도착
def exit_maze(maze):
    '''
    DFS 기반으로 탐색
    '''
    # 출발점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                row, col = i, j
    # 시작점 추가
    stack = [(row, col)]
    discovered = []
    while stack:
        row, col = stack.pop()
        if (row, col) not in discovered:
            discovered.append((row, col))
            # 우 하 좌 상
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni = row + di
                nj = col + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if maze[ni][nj] == 0:
                        stack.append((ni, nj))
                    elif maze[ni][nj] == 3:
                        return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {exit_maze(maze)}')