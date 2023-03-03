from collections import deque


# main
M, N = map(int, input().split())  # 가로, 세로
data = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

q = deque()
# 익은 토마토 탐색
for i in range(N):
    for j in range(M):
        # 익은 토마토 큐에 추가
        if data[i][j] == 1:
            q.append((i, j))
# 주변 토마토 익히기(bfs)
while q:
    i, j = q.popleft()
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ni = i + di
        nj = j + dj
        # 유효한 인덱스, 익지 않은 토마토이면
        if 0 <= ni < N and 0 <= nj < M and data[ni][nj] == 0:
            # 이전 값보다 +1 (날짜 카운팅)
            data[ni][nj] = data[i][j] + 1
            q.append((ni, nj))


def check_tomato(data):
    # 토마토가 다 익었나 검사
    max_date = 0
    for i in range(N):
        for j in range(M):
            # 안 익은 토마토가 있다면 답은 -1
            if data[i][j] == 0:
                return -1
            max_date = max(max_date, data[i][j])
    return max_date - 1

print(check_tomato(data))
