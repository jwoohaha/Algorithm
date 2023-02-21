import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


# 0은 통로, 1은 벽, 2는 출발, 3은 도착
def bfs_maze(maze):
    '''
    maze: 미로 2차원 리스트 16X16
    return: 도착 가능 1, 불가능 0
    '''
    # 시작점 추가
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                row, col = i, j
    queue = [[row, col]]  # 행, 열
    visited = []
    # bfs
    while queue:
        row, col = queue.pop(0)
        if (row, col) not in visited:
            visited.append((row, col))
            # 우 하 좌 상 인접 통로 탐색
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni = row + di
                nj = col + dj
                if 0 <= ni < 16 and 0 <= nj < 16:
                    # 통로라면 큐에 추가
                    if maze[ni][nj] == 0:
                        queue.append([ni, nj])
                    # 도착하면 거리를 리턴
                    elif maze[ni][nj] == 3:
                        return 1
    return 0


for _ in range(10):
    tc = int(input())
    maze = []
    for _ in range(16):
        num_str = input()
        num_list = []
        for char in num_str:
            num_list.append(int(char))
        maze.append(num_list)

    print(f'#{tc} {bfs_maze(maze)}')
