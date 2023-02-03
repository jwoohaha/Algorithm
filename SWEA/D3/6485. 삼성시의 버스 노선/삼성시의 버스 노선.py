
T = int(input())
for test_case in range(1, T+1):
    N = int(input())  # 버스 노선
    stops = [0] * 5001  # 정류장에 다니는 버스 노선 카운트

    for i in range(N):
        A, B = map(int, input().split())  # 다니는 정류장 정보
        for j in range(A, B+1):
            stops[j] += 1

    P = int(input())
    results = []
    for _ in range(P):
        C = int(input())  # 조회하는 정류장
        results.append(stops[C])

    print(f'#{test_case}', *results)
