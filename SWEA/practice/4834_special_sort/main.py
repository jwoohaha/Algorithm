import sys
sys.stdin = open('input.txt', 'r')



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    ssort_nums = []

    while nums:
        # 가장 큰 수, 가장 작은 수를 번갈아 nums에서 뺀 다음 리스트에 추가
        max_num = nums[0]
        max_idx = 0
        for i in range(len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
                max_idx = i
        ssort_nums.append(nums.pop(max_idx))

        min_num = nums[0]
        min_idx = 0
        for i in range(len(nums)):
            if nums[i] < min_num:
                min_num = nums[i]
                min_idx = i
        ssort_nums.append(nums.pop(min_idx))

    print(f'#{tc}', *ssort_nums[:10])
