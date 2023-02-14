import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


def iteraive_dfs(start_v):
    '''
    :param start_v: 시작점
    :return: discovered
    '''
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

def recursive_dfs(v, discovered = []):
    '''
    :param v: vertex(꼭지점)
    :param discovered: 방문한 vertex
    :return: discovered
    '''
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered

vertex, edge = map(int, input().split())
connections_list = list(map(int, input().split()))
graph = [[] for _ in range(vertex+1)]
for i in range(edge):
    graph[connections_list[i*2]].append(connections_list[(i*2)+1])

print(iteraive_dfs(1))
print(recursive_dfs(1))