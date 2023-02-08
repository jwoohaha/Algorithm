import sys
sys.stdin = open('input.txt', 'r')



T = 10
for _ in range(1, T+1):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    for start in range(100):
        i = 0  # 행(세로)
        j = start  # 열(가로)
        if data[0][start] == 0:
            continue

        while i < 99:
            # 제일 아래층에 도달할 때 까지
            if j > 0 and data[i][j-1] == 1:
                # 왼쪽 방향 전환
                while j > 0 and data[i][j-1] == 1:
                    j -= 1
                i += 1


            elif j < 99 and data[i][j+1] == 1:
                # 오른쪽 방향 전환
                while j < 99 and data[i][j+1] == 1:
                    j += 1
                i += 1


            else:
                i += 1

        if data[i][j] == 2:
            print(f'#{tc}', start)
            break
