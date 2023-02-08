def seat_assign(C, R, K):
    '''
    :param C: 가로
    :param R: 세로
    :param K: 대기번호
    :return: k번 사람의 좌석, 배정 불가인 경우 0
    '''
    row = 0
    col = 1
    num = 0

    if (C+1) * R < K:
        return 0

    else:
        while True:
            for i in range(R):
                # up
                row += 1
                num += 1
                if num == K:
                    return f'{col} {row}'
            R -= 1

            for i in range(C):
                # right
                col += 1
                num += 1
                if num == K:
                    return f'{col} {row}'
            C -= 1

            for i in range(R):
                # down
                row -= 1
                num += 1
                if num == K:
                    return f'{col} {row}'
            R -= 1

            for i in range(C):
                # left
                col -= 1
                num += 1
                if num == K:
                    return f'{col} {row}'
            C -= 1

C, R = map(int, input().split())
C -= 1
K = int(input())  # 대기번호
print(seat_assign(C, R, K))