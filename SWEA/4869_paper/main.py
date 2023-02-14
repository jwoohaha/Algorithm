import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input()) // 10
    fat = N // 2
    ans = 0
    for i in range(fat, 0, -1):
        ans += (2**i) * factorial(N-i) // factorial(N-i*2) // factorial(i)
    ans += 1
    print(f'#{tc} {ans}')