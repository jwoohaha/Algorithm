import sys
sys.stdin = open('input.txt', 'r')


def calc_node(n):
    token = nodes[n][1]
    if token.isdigit():
        return int(token)
    else:
        if token == '+':
            return calc_node(int(nodes[n][2])) + calc_node(int(nodes[n][3]))
        elif token == '-':
            return calc_node(int(nodes[n][2])) - calc_node(int(nodes[n][3]))
        elif token == '*':
            return calc_node(int(nodes[n][2])) * calc_node(int(nodes[n][3]))
        elif token == '/':
            return calc_node(int(nodes[n][2])) // calc_node(int(nodes[n][3]))

T = 10
for tc in range(1, T+1):
    # 정점의 개수
    N = int(input())
    # 인덱스 맞추기용 dummy 추가
    nodes = [0] + [input().split() for _ in range(N)]
    result = calc_node(1)
    print(f'#{tc} {result}')
