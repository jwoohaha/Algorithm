import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


def bfs_shortest_path(graph, start, goal):
    '''
    graph[dict[list]]: 그래프 정보
    start[int]: 시작 노드
    goal[int]: 도착 노드
    return: goal까지의 최단 거리
    '''
    visited = []  # 방문한 노드 번호 리스트
    queue = [[start, 0]]  # 노드 번호, 거리
    while queue:
        v = queue.pop(0)
        # goal에 도달하면 거리 리턴
        if v[0] == goal:
            return v[1]
        elif v[0] not in visited:
            visited.append(v[0])
            # 거리 +1 후 queue에 추가
            for node in graph[v[0]]:
                queue.append([node, v[1] + 1])
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # 그래프 만들어 주기
    graph = {i: [] for i in range(V + 1)}
    for i in range(E):
        # 무향그래프에 간선 정보 추가
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    # 시작, 도착 노드
    S, G = map(int, input().split())

    print(f'#{tc} {bfs_shortest_path(graph, S, G)}')