
def count_worms(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    r = len(grid)  # row 수
    c = len(grid[0])  # col 수
    visited = set()  # 방문한 지점 저장
    stk = []
    cnt = 0  # 섬 갯수 카운트
    # grid를 탐색하며 확인
    for i in range(r):
        for j in range(c):
            # 시작점 찾기
            if (i, j) not in visited and grid[i][j] == 1:
                row, col = i, j
                visited.add((i, j))
                cnt += 1
                # bfs로 탐색
                while True:
                    # 주변 노드 탐색
                    for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:  # 상 우 하 좌
                        ni = row + di
                        nj = col + dj
                        if 0 <= ni < r and 0 <= nj < c:
                            # 방문하지 않고 땅이면 스택에 추가, 방문 표시
                            if (ni, nj) not in visited and grid[ni][nj] == 1:
                                visited.add((ni, nj))
                                stk.append((ni, nj))
                    if not stk:
                        break
                    row, col = stk.pop()
    return cnt

T = int(input())
for tc in range(1, T+1):
    # 가로, 세로, 배추가 있는 위치
    M, N, K = map(int, input().split())
    # 배추 밭 세팅
    grid = [[0] * M for _ in range(N)]
    for _ in range(K):
        m, n = map(int, input().split())
        grid[n][m] = 1
    print(count_worms(grid))
