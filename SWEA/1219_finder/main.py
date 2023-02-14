import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


def iteraive_dfs(graph, start_v):
    '''
    시작점에서 dfs로 탐색하며 도착점에 들르면 1을 리턴
    다 돌아도 도착하지 못하면 0을 리턴
    :param graph: 탐색 대상 그래프
    :param start_v: 시작점
    :return: 1(success) / 0(fail)
    '''
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v == 99:
            return 1
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return 0

while True:
    try:
        tc, edge = map(int, input().split())
    # 입력이 없는데 계속 받을 경우 break
    except EOFError:
        break

    connections_list = list(map(int, input().split()))
    graph = {i: [] for i in range(100)}
    # edge 정보 추가
    for i in range(edge):
        graph[connections_list[i*2]].append(connections_list[(i*2)+1])
    print(f'#{tc}', iteraive_dfs(graph, 0))

