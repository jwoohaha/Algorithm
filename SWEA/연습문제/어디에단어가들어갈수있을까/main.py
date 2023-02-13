import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N * N 단어퍼즐, K 단어 길이
    matrix = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0  # 들어갈 수 있는 자리의 수
    size_list = []  # 빈 자리의 길이를 저장하는 리스트

    for i in range(N):
        # 행 방향 체크
        blank_size = 0  # 들어갈 자리의 길이
        for j in range(N):
            if matrix[i][j] == 1:
                # 수가 1이면 빈 자리의 길이를 +1
                blank_size += 1
                if j == N-1:
                    # 마지막 인덱스 일 때 빈 자리 길이 리스트에 추가
                    size_list.append(blank_size)

            elif blank_size != 0:
                # 0이 나오면 빈 자리 길이 리스트에 추가
                size_list.append(blank_size)
                blank_size = 0

    for j in range(N):
        # 열 방향 체크
        blank_size = 0  # 들어갈 자리의 길이
        for i in range(N):
            if matrix[i][j] == 1:
                # 수가 1이면 빈 자리의 길이를 +1
                blank_size += 1
                if i == N-1:
                    # 마지막 인덱스 일 때 빈 자리 길이 리스트에 추가
                    size_list.append(blank_size)

            elif blank_size != 0:
                # 0이 나오면 빈 자리 길이 리스트에 추가
                size_list.append(blank_size)
                blank_size = 0
    # 빈 자리 길이를 저장한 리스트에서 K 길이의 자리 수를 셈
    cnt += size_list.count(K)


    print(f'#{tc} {cnt}')

