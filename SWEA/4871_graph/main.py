import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')

def iteraive_dfs(start_v, end_v):
    '''
    시작점에서 dfs로 탐색하며 도착점에 들르면 1을 리턴
    다 돌아도 도착하지 못하면 0을 리턴
    :param start_v: 시작점
    :param end_v: 도착점
    :return: 1(success) / 0(fail)
    '''
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v == end_v:
            return 1
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 그래프 만들어 주기
    graph = {i: [] for i in range(V+1)}
    for i in range(E):
        # 그래프에 간선 정보 추가
        start, end = map(int, input().split())
        graph[start].append(end)

    # 경로의 존재를 확인할 출발, 도착노드
    S, G = map(int, input().split())
    print(f'#{tc}', iteraive_dfs(S, G))

