import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')

# 0은 통로, 1은 벽, 2는 출발, 3은 도착
def bfs_iterative(N, maze):
    # 시작점 추가
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                row, col = i, j
    queue = [[row, col, -1]]  # 행, 열, 거리
    visited = []
    # bfs
    while queue:
        row, col, distance = queue.pop(0)
        if (row, col) not in visited:
            visited.append((row, col))
            distance += 1
            # 우 하 좌 상 인접 통로 탐색
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni = row + di
                nj = col + dj
                if 0 <= ni < N and 0 <= nj < N:
                    # 통로라면 큐에 추가
                    if maze[ni][nj] == 0:
                        queue.append([ni, nj, distance])
                    # 도착하면 거리를 리턴
                    elif maze[ni][nj] == 3:
                        return distance
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = []
    for _ in range(N):
        num_str = input()
        num_list = []
        for char in num_str:
            num_list.append(int(char))
        maze.append(num_list)

    print(f'#{tc} {bfs_iterative(N, maze)}')


