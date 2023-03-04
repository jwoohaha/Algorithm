from collections import deque


def bfs(start):
    q = deque()
    # 위치와 시간
    q.append([start, 0])
    while q:
        x = q.popleft()
        # 동생을 찾으면 시간 리턴
        if x[0] == K:
            return x[1]
        for next in (x[0]-1, x[0]+1, x[0]*2):
            if 0 <= next < 100001 and not visited[next]:
                q.append([next, x[1]+1])
                visited[next] = 1  # 방문 표시


# main
N, K = map(int, input().split())  # 수빈, 동생의 위치
visited = [0] * 100001  # 방문 표시
print(bfs(N))