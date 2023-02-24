import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


def pre_order(n):
    # 트리를 순회하며 서브 트리 노드의 개수를 카운트
    global cnt
    if n > 0:
        cnt += 1
        pre_order(left[n])
        pre_order(right[n])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())  # 간선의 개수, 서브 트리 루트 노드
    edges = list(map(int, input().split()))
    # 인덱스는 부모노드, 자식 노드의 번호를 저장
    left = [0] * (E+2)
    right = [0] * (E+2)
    cnt = 0  # 서브 트리 노드 개수 카운트
    # 트리 만들어주기
    for i in range(E):
        parent = edges[i * 2]
        child = edges[i * 2 + 1]
        if not left[parent]:
            left[parent] = child
        else:
            right[parent] = child
    pre_order(N)
    print(f'#{tc} {cnt}')
