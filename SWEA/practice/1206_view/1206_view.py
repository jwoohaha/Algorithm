for t in range(1, 11): # test case 10개
    buildings_num = int(input())
    buildings = list(map(int, input().split()))
    result = 0
 
    i = 2
    while i < buildings_num-2:
        if max(buildings[i-2:i+3]) == buildings[i]:
            # 좌2우2 중 최대 높이이면
            second_high = max(buildings[i-2:i] + buildings[i+1:i+3])
            # 조망권 확보 세대는 2번째 높은 층 위 세대들
            result += buildings[i] - second_high
            i += 3
        else:
            i += 1
 
    print(f'#{t} {result}')