import sys
sys.stdin = open('input.txt', 'r')



T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    result = 0
    for i in range(1, 1<<10):  # 0인 경우는 제외해야 하므로 1에서 시작
        subset = []
        for j in range(10):
            if i & (1 << j):
                subset.append(nums[j])
        if sum(subset) == 0:
            result = 1
    print(f'#{tc} {result}')
