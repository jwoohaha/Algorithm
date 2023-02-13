import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


T = 10
for _ in range(1, T+1):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    results = []  # 결과 리스트 (출발 인덱스, 거리)

    for start in range(100):
        i = 0  # 행(세로)
        j = start  # 열(가로)
        distance = 0  # 이동거리

        if data[0][start] == 0:
            continue

        while i < 99:
            # 제일 아래층에 도달할 때 까지
            if j > 0 and data[i][j-1] == 1:
                # 왼쪽 방향 전환
                while j > 0 and data[i][j-1] == 1:
                    j -= 1
                    distance += 1
                i += 1
                distance += 1


            elif j < 99 and data[i][j+1] == 1:
                # 오른쪽 방향 전환
                while j < 99 and data[i][j+1] == 1:
                    j += 1
                    distance += 1
                i += 1
                distance += 1


            else:
                # 아래로 내려감
                i += 1
                distance += 1

        results.append((start, distance))
    # distance가 최소인 튜플을 찾고 인덱스 출력
    shortest = min(results, key=lambda x: x[1])
    print(f'#{tc} {shortest[0]}')

