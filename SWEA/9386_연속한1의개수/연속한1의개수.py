T = int(input())
for test_case in range(1, T+1):
    nums_len = int(input())
    nums = input()
    cnt = max_cnt = 0
    # 수 2개를 비교하며 1이 연속하는지 카운트
    for i in range(nums_len):
        if nums[i] == '1':
            cnt += 1
            max_cnt = max(cnt, max_cnt)
        else:
            cnt = 0
 
    print(f'#{test_case} {max_cnt}')