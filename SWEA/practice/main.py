# import sys
# sys.stdin = open('input.txt', 'r')


def n_queens(i, col):
    global cnt
    n = len(col) -1
    if (promising(i, col)):
        # 모두 탐색하면(정답을 찾으면) cnt +1
        if (i == n):
            cnt += 1
            return
        else:
            # 열 방향 탐색
            for j in range(1, n+1):
                # 다음 행으로 이동
                col[i+1] = j
                n_queens(i+1, col)


def promising(i, col):
    k = 1
    flag = True
    while (k < i and flag):
        # 열이 같거나 대각선에 겹치는 게 없으면
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            flag = False
        k += 1
    return flag

N = int(input())
col = [0] * (N+1)
cnt = 0
n_queens(0, col)
print(cnt)
