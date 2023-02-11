T = int(input())
for test_case in range(1, T+1):
    D, A, B, F = map(int, input().split())  # 거리, A 속력, B 속력, 파리의 속력
    time = D / (A + B)
    fly_distance = time * F
    print(f'#{test_case} {fly_distance}')