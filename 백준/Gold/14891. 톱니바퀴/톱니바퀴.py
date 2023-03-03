from collections import deque


def rotate(gear, dir):
    '''
    해당 톱니바퀴를 dir에 따라 회전 시킴
    gear: List[int]
    dir: int  1: 시계방향, -1: 반시계방향
    '''
    # 시계방향
    if dir == 1:
        gear.appendleft(gear.pop())
    elif dir == -1:
        gear.append(gear.popleft())


def dfs(g, d):
    '''
    해당 톱니바퀴와 조건에 맞는 주위 톱니바퀴를 회전
    g: 톱니 바퀴의 인덱스
    d: 회전 방향
    '''
    check[g] = 1
    left = g - 1
    right = g + 1
    # 가장 왼쪽 톱니가 아니면 왼쪽 톱니와 비교, 미방문시 탐색
    if g > 1:
        if gears[left][2] != gears[g][6] and check[left] == 0:
            dfs(left, -d)
    # 가장 오른쪽 톱니가 아니면 오른쪽 톱니와 비교, 미방문시 탐색
    if g < 4:
        if gears[right][6] != gears[g][2] and check[right] == 0:
            dfs(right, -d)

    rotate(gears[g], d)


# main
gears = deque()
gears.appendleft(0)  # 인덱스 편의를 위한 dummy
# 인풋처리
for i in range(4):
    num_str = input()
    nums = deque()
    for char in num_str:
        nums.append(int(char))
    gears.append(nums)

# bfs 탐색 시행
K = int(input())
for _ in range(K):
    g, d = map(int, input().split())  # 톱니바퀴 번호, 방향
    check = [0] * 5  # 방문 표시
    dfs(g, d)

# 점수 구하기
ans = 0
for i in range(1, 5):
    if gears[i][0] == 1:
        ans += 2 ** (i-1)
print(ans)
