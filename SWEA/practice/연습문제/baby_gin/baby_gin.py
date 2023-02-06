T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input()))
    # 수가 몇 개 있는지 세는 리스트
    cnt_num = [0] * 12  # run 검사 편의를 위해 더미 2개 추가
    for num in nums:
        cnt_num[num] += 1

    tri = run = 0
    result = 0
    i = 0

    while i < 10:
        # tri가 두 번 연속 있을 수도 i 편하게 제어 하기 위해 while문 사용
        if cnt_num[i] >= 3:
            # tri 검사
            cnt_num[i] -= 3
            tri += 1
            continue

        if cnt_num[i] >= 1 and cnt_num[i+1] >= 1 and cnt_num[i+2] >= 1:
            # run 검사
            cnt_num[i] -= 1
            cnt_num[i+1] -= 1
            cnt_num[i+2] -= 1
            run += 1
            continue
        i += 1

    if tri + run == 2:
        result = 1

    print(f'#{tc} {result}')