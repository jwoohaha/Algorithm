T = int(input())
for test_case in range(1, T+1):
    N = int(input())  # 노선의 수
    cnt = [0] * 1001
 
    for _ in range(N):
        #  1 일반, 2 급행, 3 광역
        BUS, A, B = map(int, input().split())  # 버스타입, 출발 정류장, 종점
        cnt[B] += 1  # 종점은 무조건 방문
         
        if BUS == 1:  # 일반
            for i in range(A, B):
                cnt[i] += 1
                 
        elif BUS == 2:  # 급행
            for i in range(A, B, 2):
                cnt[i] += 1
                 
        else:  # 광역
            if A % 2 == 0:
                cnt[A] += 1  # 시작점은 무조건 방문
                for i in range(A+1, B):
                    if i % 4 == 0:
                        cnt[i] += 1
 
            if A % 2 == 1:
                cnt[A] += 1  # 시작점은 무조건 방문
                for i in range(A+1, B):
                    if i % 3 == 0 and i % 10 != 0:
                        cnt[i] += 1
 
    print(f'#{test_case}', max(cnt))