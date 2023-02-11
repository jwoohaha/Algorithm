T = int(input())
for tc in range(1, T+1):
    num_length = int(input())
    nums = list(map(int, input().split()))
    max_fall = 0

    for i in range(num_length):
        # nums의 요소를 돌며
        # 해당 박스 더미 최고점의 낙차를 체크 (최고점의 낙차가 최대값)
        fall = 100 - i  # 아무것도 없을 때 낙차
        height = nums[i] # 최고점
        for idx in range(i, num_length):
            # 해당 높이에 다른 박스가 있으면 낙차 1 감소
            if nums[idx] >= height:
                fall -= 1
        # 최대값 업데이트
        max_fall = max(max_fall, fall)

    print(f'#{tc} {max_fall}')