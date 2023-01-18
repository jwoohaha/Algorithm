# 체스판 다시 칠하기

# 인풋
M, N = map(int, input().split())

# 기본 보드 설정
chessboard_1 = []
chessboard_2 = []
line_1 = 'BWBWBWBW'
line_2 = 'WBWBWBWB'
for i in range(8):
    if i % 2 ==0:
        chessboard_1.append(line_1)
        chessboard_2.append(line_2)
    else:
        chessboard_1.append(line_2)
        chessboard_2.append(line_1)

# 인풋 보드
found_board = []
for k in range(M):
    found_board.append(input())

# 기본 보드와 인풋 보드 비교 칠해야 하는 수 찾기
cnt = 64
tmp = 0
tmp1 = 0
tmp2 = 0
for j in range(N-7): # col
    for i in range(M-7): # row
        for row in range(8):
            for col in range(8):
                if found_board[row+i][col+j] != chessboard_1[row][col]:
                    tmp1 +=1
                if found_board[row+i][col+j] != chessboard_2[row][col]:
                    tmp2 +=1

        tmp = min(tmp1, tmp2)
        if tmp < cnt:
            cnt = tmp
        tmp = 0
        tmp1 = 0
        tmp2 = 0
print(cnt)