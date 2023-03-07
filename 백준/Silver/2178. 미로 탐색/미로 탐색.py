from collections import deque

# 미로의 크기이자 도착점
N, M = map(int, input().split())
data = [[] for _ in range(N)]
for i in range(N):
    nums = input()
    for num in nums:
        data[i].append(int(num))


def bfs(si=0, sj=0):
    q = deque([(si, sj)])
    didj = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while q:
        si, sj = q.popleft()
        for di, dj in didj:
            ni = si + di
            nj = sj + dj
            # 유효한 인덱스, 미방문
            if 0 <= ni < N and 0 <= nj < M and data[ni][nj] == 1:
                data[ni][nj] = data[si][sj] + 1
                q.append((ni, nj))


bfs()
print(data[N-1][M-1])
