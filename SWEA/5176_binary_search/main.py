import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


def in_order(node):
    # 중위 순회 이용
    global cnt
    if node <= N:
        # left
        in_order(node * 2)
        # root
        nodes[node] = cnt
        cnt += 1
        #right
        in_order(node * 2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nodes = [0 for i in range(N + 1)]
    cnt = 1
    in_order(1)
    print(f'#{tc} {nodes[1]} {nodes[N//2]}')
