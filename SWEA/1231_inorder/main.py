import sys
sys.stdin = open('input.txt', 'r')


def inorder(n):
    '''
    left -> root -> right 순으로 tree를 탐색
    '''
    # 왼쪽 맨 아래까지 내려감
    if n * 2 <= N:
        inorder(n * 2)
    print(data[n][1], end='')
    # 오른쪽 아래로 내려감
    if n * 2 + 1 <= N:
        inorder(n * 2 + 1)


T = 10
for tc in range(1, T + 1):
    N = int(input())
    # 해당 정점의 문자, 왼쪽 자식, 오른쪽 자식
    data = [input().split() for _ in range(N)]

    data.insert(0, 'dummy')

    print(f"#{tc}", end=' ')
    inorder(1)
    print()