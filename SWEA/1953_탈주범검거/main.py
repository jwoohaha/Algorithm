import sys
sys.stdin = open('input.txt', 'r')


# 0, 1, 2, 3 상 하 좌 우
# 터널 타입(타입 1이면 인덱스1, 상하좌우로 움직일 수 있음)
type = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
# 새로 이동하는 곳과 터널 연결 확인을 위한 딕셔너리 (현 위치에서 위로 이동하면 그 윗 터널은 아래와 연결 되어 있어야 함)
opp = {0: 1, 1: 0, 2: 3, 3: 2}
didj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(sr, sc, l):
    q = []
    q.append((sr, sc))
    visited = [[0]*M for _ in range(N)]
    visited[sr][sc] = 1
    cnt = 1

    while q:
        r, c = q.pop(0)
        if visited[r][c] == l:
            return cnt

        t = data[r][c]  # 터널의 타입
        for move in type[t]:
            di, dj = didj[move]
            ni = r + di
            nj = c + dj
            # 유효한 인덱스, 이전에 방문하지 않고, 연결 되어 있다면
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 \
                    and opp[move] in type[data[ni][nj]]:
                q.append((ni, nj))
                # 시간 체크
                visited[ni][nj] = visited[r][c]+1
                # 이동 가능 자리 +1
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    # 터널 크기 세로, 가로, 맨홀 세로, 가로, 소요시간
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(R, C, L)
    print(f'#{tc} {ans}')
