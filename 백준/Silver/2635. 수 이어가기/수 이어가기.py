N = int(input())
len_max = 0
max_nums = []

for i in range(N//2, N+1):
    # 두 번째 수를 바꿔가며 최대 개수의 수일 경우를 탐색
    nums = [N, i]
    # 규칙에 따라 수를 계속 추가
    while True:
        num = nums[-2] - nums[-1]
        if num < 0:
            break
        nums.append(num)
    # 개수가 최대이면 업데이트
    if len(nums) > len_max:
        len_max = len(nums)
        max_nums = nums

print(len_max)
print(*max_nums)