def n_queens(depth):
    global cnt
    # 맨 아래까지 도달하면 가능 횟수 cnt + 1
    if depth == n:
        cnt += 1
        return
    else:
        # 열 방향 탐색
        for j in range(n):
            # 해당 열 점유 표시
            col[depth] = j
            if promising(depth):
                n_queens(depth+1)


def promising(depth):
    for i in range(depth):
        # 열이 같거나 대각선에 겹치는 게 있으면 false
        if col[depth] == col[i] or abs(col[depth] - col[i]) == abs(depth - i):
            return False
    return True


n = int(input())
col = [0] * (n+1)
cnt = 0
n_queens(0)
print(cnt)