T = int(input())
for test_case in range(1, T+1):
    nums_len = int(input())
    carrots_size = list(map(int, input().split()))
    cnt = 1
    max_cnt = 1
    # 수 2개를 비교하며 오름차순 카운트
    for i in range(nums_len - 1):
        if carrots_size[i] < carrots_size[i+1]:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 1
 
    print(f'#{test_case} {max_cnt}')