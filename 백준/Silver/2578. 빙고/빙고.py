def check_bingo(data):
    '''
    data로 받은 빙고판에 선이 3개 이상 그어져있는지 판별
    return: bool
    '''
    status = False
    diag_down = 0
    diag_up = 0
    bingo = 0
    for i in range(5):
        # 가로 방향 확인
        if sum(data[i]) == 0:
            bingo += 1
        # 세로 방향 확인
        col_sum = 0
        for j in range(5):
            col_sum += data[j][i]
        if col_sum == 0:
            bingo += 1
        # 대각선 확인
        diag_down += data[i][i]
        diag_up += data[4-i][i]
    if diag_down == 0:
        bingo += 1
    if diag_up == 0:
        bingo += 1
    # 빙고 상태 판별
    if bingo >= 3:
        status = True
    return status

def bingo_simulation(data, mc_call):
    '''
    mc가 부르는 수를 0으로 표시하며 빙고 시뮬레이션
    몇 번째 수를 불렀을 때 빙고인지 리턴
    '''
    cnt = 11  # 사회자가 부른 수의 갯수
    for num in mc_call[11:]:
        cnt += 1
        for i in range(5):
            for j in range(5):
                # 빙고판에서 사회자가 부른 수 찾기
                if data[i][j] == num:
                    data[i][j] = 0
                    # 빙고이면 카운트 리턴
                    if check_bingo(data):
                        return cnt

data = [list(map(int, input().split())) for _ in range(5)]
mc_call = []
for _ in range(5):
    mc_call += list(map(int, input().split()))
# 기본 세팅(최소 12개 부터 빙고 가능)
mc_call_11 = mc_call[:11]
for i in range(5):
    for j in range(5):
        if data[i][j] in mc_call_11:
            data[i][j] = 0

print(bingo_simulation(data, mc_call))