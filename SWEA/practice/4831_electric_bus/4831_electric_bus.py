T = int(input())
for tc in range(1, T+1):
		# 최소로 충전하는 방법은 이동 가능 거리 중 가장 먼 충전소에서 충전
    # 최대 이동 정류장 수, 목적지, 충전기 수 입력 받기
    m_limit, destination, charger_num = map(int, input().split())
    chargers = list(map(int, input().split()))

    idx = 0  # 현 위치
    cnt = 0  # 충전 횟수
    status = True  # 상태

    while status:
        if idx + m_limit >= destination:
            # 이동 가능 거리 내에 목적지 있으면 종료 후 정답 출력
            status = False

        else:
            # 거리 내에 마지막 충전기로 이동
            stk = []
            for charger in chargers:
                if charger > idx and charger <= idx + m_limit:
                    # 이동 가능 거리 안쪽 충전기 파악
                    stk.append(charger)

            if stk:
                # 최대한 먼 충전기로 이동
                idx = stk.pop()
                cnt += 1

            else:
                # 충전기 없으면 불가
                cnt = 0
                status = False
                break

    print(f'#{tc} {cnt}')