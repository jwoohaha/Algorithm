# 주사위의 수, 주사위에 적힌 숫자 정보
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
opposite_idx = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
max_sum = 0
# 가장 밑 주사위 세팅
for i in range(6):
    val = data[0][i]  # 주사위 면에 써 있는 값
    nums = {1, 2, 3, 4, 5, 6}
    nums.remove(val)
    nums.remove(data[0][opposite_idx[i]])
    # 윗 면은 4개가 가능 (회전)
    for top in nums:
        # 각 경우의 합
        tmp_sum = data[0][i]  # val
        for j in range(1, N):
            nums = {1, 2, 3, 4, 5, 6}
            # 윗 주사위의 아랫면 값은 밑 주사위의 윗면과 동일
            bottom = top
            bottom_idx = data[j].index(bottom)
            top_idx = opposite_idx[bottom_idx]
            top = data[j][top_idx]
            # 옆 면중 최대 값 선택
            side = nums - {top, bottom}
            val = max(side)
            tmp_sum += val
        max_sum = max(tmp_sum, max_sum)
print(max_sum)