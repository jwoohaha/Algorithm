import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


def rotate(magnet, dir):
    '''
    magnet을 방향에 맞게 회전
    return: None
    '''
    # 시계방향
    if dir == 1:
        magnet.appendleft(magnet.pop())
    # 반시계방향
    elif dir == -1:
        magnet.append(magnet.popleft())


def dfs(num, dir):
    # 자석을 회전시키고 양 옆 자석을 체크
    check[num] = 1
    if num < 3:
        if mag[num][2] != mag[num+1][6] and not check[num+1]:    # 자성 다를 경우
            dfs(num+1, -1*dir)              # 다음 자석 번호, 방향 반대
    if num > 0:
        if mag[num][6] != mag[num-1][2] and not check[num-1]:    # 자성 다를 경우
            dfs(num-1, -1*dir)              # 다음 자석 번호, 방향 반대
    # 양 옆 자석을 체크하고 자석을 회전
    rotate(mag[num], dir)

# main
T = int(input())
for tc in range(1, T+1):
    K = int(input())
    mag = [deque(map(int, input().split())) for _ in range(4)]
    for _ in range(K):      # K번 회전
        n, d = map(int, input().split())    # 자석 번호, 회전 방향
        check = [0] * 4
        dfs(n-1, d)

    result = 0
    for i in range(4):
        result += mag[i][0] * 2 ** i
    print(f"#{tc} {result}")
