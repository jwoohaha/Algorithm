from collections import deque

def bfs(S):
    '''
    :param s: 현재 있는 층
    :return: 목적지에 가기 위한 버튼 수 최솟값, 이동 불가시 안내문 출력
    '''
    visited = [-1] * (F + 1)
    visited[S] = 0
    q = deque([S])
    # bfs
    while q:
        curr = q.popleft()  # 현재 층
        # 도착 시 종료
        if curr == G:
            return visited[curr]
        up = curr + U
        down = curr - D
        if up <= F and visited[up] == -1:
            visited[up] = visited[curr] + 1
            q.append(up)
        if down > 0 and visited[down] == -1:
            visited[down] = visited[curr] + 1
            q.append(down)
    warning = 'use the stairs'
    return warning

# 건물높이, 현재 있는 층, 목적지, u층 위로 이동, d층 아래로 이동
F, S, G, U, D = map(int, input().split())

print(bfs(S))