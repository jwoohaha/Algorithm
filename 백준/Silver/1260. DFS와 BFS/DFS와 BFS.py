from collections import deque


def dfs(x, visited=[]):
    '''
    :param x: int 방문할 노드 번호
    :param visited: list 방문한 노드 순서
    :return: visited
    '''
    visited.append(x)
    next_nodes = graph[x]
    # 노드 번호가 작은 것을 먼저 방문
    next_nodes.sort()

    if not next_nodes:
        return visited

    for node in next_nodes:
        if node not in visited:
            visited = dfs(node, visited)

    return visited


def bfs(x):
    '''
    :param x: int 시작 노드 번호
    :return: visited
    '''
    visited = [x]
    q = deque([x])
    while q:
        v = q.popleft()
        next_nodes = graph[v]
        # 노드 번호가 작은 것을 먼저 방문
        next_nodes.sort()
        for w in next_nodes:
            if w not in visited:
                visited.append(w)
                q.append(w)
    return visited


# main
N, M, V = map(int, input().split())  # 정점, 간선, 탐색 시작 번호
graph = {i: [] for i in range(N+1)}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
print(*dfs(V))
print(*bfs(V))