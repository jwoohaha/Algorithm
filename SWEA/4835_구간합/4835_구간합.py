T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 배열의 길이, M: 이웃한 M개의 합 구하기
    nums = list(map(int, input().split()))
		# 초기값 설정
    max_sum = sum(nums[0:M])
    min_sum = sum(nums[0:M])
    for i in range(N-M+1):
        # 구간합 최대 최소 탐색
        max_sum = max(sum(nums[i:i+M]), max_sum)
        min_sum = min(sum(nums[i:i+M]), min_sum)
        
    result = max_sum - min_sum
    print(f'#{tc} {result}')