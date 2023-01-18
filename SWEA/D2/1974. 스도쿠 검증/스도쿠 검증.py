

def sudoku_check(table):  # 스도쿠 규칙을 만족하는지 체크
    default_nums = set([i for i in range(1, 10)])
    success = True

    for i in range(9):  # 가로줄 체크
        if set(table[i]) != default_nums:
            success = False

    for j in range(9):  # 세로줄 체크
        vertical_line = []
        for i in range(9):
            vertical_line.append(table[i][j])
        if set(vertical_line) != default_nums:
            success = False

    for i in range(3):  # 3X3 9칸 체크
        for j in range(3):
            box = []
            for k in range(3):
                for l in range(3):
                    box.append(table[k+(3*i)][l+(3*j)])
            if set(box) != default_nums:
                success = False

    return success

# 인풋처리
T = int(input())

for t in range(T):
    sudoku_table = [[0]*9 for _ in range(9)] # 2차원 리스트 생성
    for i in range(9):
        nums = list(map(int, input().split()))
        sudoku_table[i] = nums

    if sudoku_check(sudoku_table):
        print(f'#{t+1} 1')

    else:
        print(f'#{t+1} 0')
