import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    # 노드의 개수, 리프 노드의 개수, 출력할 노드 번호
    N, M, L = map(int, input().split())
    nodes = [0] * (N+1)
    for i in range(M):
        leaf_node_num, val = map(int, input().split())
        nodes[leaf_node_num] = val
    # N이 짝수면 맨 마지막 리프 노드의 부모는 자식이 하나
    if N % 2 == 0:
        nodes[N // 2] = nodes[N]
        N -= 1
    # 리프 노드의 합을 부모 노드에 저장
    for i in range(N-M, 0, -1):
        nodes[i] = nodes[i*2] + nodes[i*2+1]

    print(f'#{tc} {nodes[L]}')