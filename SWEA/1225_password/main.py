import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


def password_gen(nums):
    while True:
        for i in range(1, 6):
            tmp = nums.pop(0) - i
            # 0보다 작거나 같을 경우 해당 배열이 패스워드
            if tmp <= 0:
                nums.append(0)
                return nums
            else:
                nums.append(tmp)

while True:
    try:
        tc = int(input())
        nums = list(map(int, input().split()))
    except EOFError:
        break



    print(f'#{tc}', end=' ')
    print(*password_gen(nums))

