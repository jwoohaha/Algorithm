T = int(input())
divs = [2, 3, 5, 7, 11]
for test_case in range(1, T+1):
    ans = [0] * 5
    num = int(input())
    for i in range(len(divs)):
        while (num % divs[i]) == 0:
            # 나눠지면 소인수의 지수 +1
            num //= divs[i]
            ans[i] += 1
 
    print(f'#{test_case}', *ans)