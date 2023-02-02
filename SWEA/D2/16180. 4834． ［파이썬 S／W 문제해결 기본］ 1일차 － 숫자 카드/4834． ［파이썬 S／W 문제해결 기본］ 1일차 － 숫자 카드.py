T = int(input())
for tc in range(1, T+1):
    num_len = int(input())
    nums = list(map(int, input()))
    cnt_num = [0] * 10

    for num in nums:
        # 각 수가 몇 개 있는지 셈
        cnt_num[num] += 1

    max_num = 0  # 가장 많은 카드의 숫자
    max_cnt = 0  # 장 수
    for i in range(10):
        # cnt_num을 돌며 제일 많은 수와 장 수 찾기
        if cnt_num[i] >= max_cnt:
            max_cnt = cnt_num[i]
            max_num = i

    print(f'#{tc} {max_num} {max_cnt}')
