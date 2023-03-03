import sys
sys.stdin = open('input.txt', 'r')


# main
N, M = map(int, input().split())  # 정점의 개수, 간선의 개수
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)
# 그래프 생성
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(i):
    visited[i] = True
    for w in graph[i]:
        if not visited[w]:
            dfs(w)
    return


# 아직 방문하지 못한 점을 만나면 분리된 component -> cnt + 1
component_cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        component_cnt += 1
        dfs(i)

print(component_cnt)
