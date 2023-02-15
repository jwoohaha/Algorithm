width, height = map(int, input().split())  # 가로 세로
N = int(input())  # 상점의 개수
stores = []
result = 0

# 위치: 방향, 거리(왼쪽, 위쪽 기준)
for _ in range(N):
    sect, dist = map(int, input().split())
    stores.append((sect, dist))

sect, dist = map(int, input().split())  # 동근이의 위치
for store in stores:
    # 동근이 북쪽
    if sect == 1:
        if store[0] == 1:
            tmp = abs(dist - store[1])
        elif store[0] == 3:
            tmp = dist + store[1]
        elif store[0] == 2:
            tmp = height + min(dist + store[1], (width - dist) + (width - store[1]))
        else:
            tmp = width - dist + store[1]
        result += tmp
    # 동근이 서쪽
    elif sect == 3:
        if store[0] == 3:
            tmp = abs(dist - store[1])
        elif store[0] == 2:
            tmp = height - dist + store[1]
        elif store[0] == 4:
            tmp = width + min(dist+store[1], (height-dist)+(height-store[1]))
        else:
            tmp = dist + store[1]
        result += tmp
    # 동근이 남쪽
    elif sect == 2:
        if store[0] == 2:
            tmp = abs(dist - store[1])
        elif store[0] == 4:
            tmp = width - dist + height - store[1]
        elif store[0] == 1:
            tmp = height + min(dist+store[1], (width-dist)+(width-store[1]))
        else:
            tmp = dist + height - store[1]
        result += tmp
    # 동근이 동쪽
    else:
        if store[0] == 4:
            tmp = abs(dist - store[1])
        elif store[0] == 1:
            tmp = width - store[1] + dist
        elif store[0] == 3:
            tmp = width + min(dist+store[1], (height-dist)+(height-store[1]))
        else:
            tmp = width - store[1] + height - dist
        result += tmp
print(result)