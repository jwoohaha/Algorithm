import sys
sys.stdin = open('input.txt', 'r')


def dfs(row, col, cnt, flag):
    global ans
    ans = max(ans, cnt)
    # 우 하 좌 상 인접 통로 탐색
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni = row + di
        nj = col + dj
        # 유효한 인덱스
        if 0 <= ni < N and 0 <= nj < N:
            # 이동 가능하다면 이동
            if data[row][col] > data[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                dfs(ni, nj, cnt+1, flag)
                visited[ni][nj] = 0  # 추후 탐색을 위한 초기화
            # 이동 불가능하고 공사가 가능하다면 공사 후 이동
            elif data[row][col] <= data[ni][nj] and flag:
                for i in range(1, K+1):
                    data[ni][nj] -= i  # 공사
                    flag = False  # 공사 불가
                    # 높이가 낮음, 방문하지 않음
                    if data[row][col] > data[ni][nj] and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        dfs(ni, nj, cnt+1, flag)
                        visited[ni][nj] = 0
                    # 공사 취소
                    data[ni][nj] += i
                    flag = True


# main
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # 한 변의 길이, 최대 공사 가능 깊이
    data = [list(map(int, input().split())) for _ in range(N)]  # 지도 정보
    # 최고 높이 찾기
    top = 0
    for i in range(N):
        for j in range(N):
            top = max(top, data[i][j])
    # 봉우리에서 dfs 시작
    ans = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == top:
                visited = [[0]*N for _ in range(N)]
                visited[i][j] == 1
                dfs(i, j, 0, True)

    print(f'#{tc} {ans+1}')
