# 에라토스테네스의 체

def get_prime_numbers(n):  # n미만 소수들 리턴
    sieve = [True] * n
    limit = int(n ** 0.5) + 1  # n제곱근 미만 고려(만약 n보다 작은 어떤 수 m이 m=ab면 a와 b중 적어도 하나는 루트n 이하)
    for i in range(2, limit):
        if sieve[i] == True:
            for j in range(i*2, n, i):  # i의 배수 지우기
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]


N = int(input())
nums = list(map(int, input().split()))
max_num = max(nums)
prime_numbers = get_prime_numbers(max_num+1)
prime_number_cnt = 0
for num in nums:
    if num in prime_numbers:
        prime_number_cnt += 1
print(prime_number_cnt)