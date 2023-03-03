

def dfs(v, visited):
    '''
    v: 탐색 노드 번호
    visited: 탐색 한 노드
    '''
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            visited = dfs(w, visited)
    return visited


# main
N = int(input())  # 컴퓨터의 수
E = int(input())  # 간선의 수
# 그래프 만들어 주기
graph = {i: [] for i in range(N+1)}
for _ in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
infected = dfs(1, [])
infected.pop(0)  # 1번 컴퓨터 제외
print(len(infected))
