T = int(input())

for tc in range(1, T+1):
    num_length = int(input())
    nums = list(map(int, input().split()))
		# 초기값 설정
    min_num = nums[0]
    max_num = nums[0]
    for num in nums:
				# 숫자 리스트를 돌며 최대 최소값 체크
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    result = max_num - min_num
    print(f'#{tc} {result}')