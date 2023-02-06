'''
입력을 받아 층(높이)에 따라 상자의 개수를 파악
dump 수 만큼 최고 층에서 -1, 최저 층에 +1
'''

T = 10
for tc in range(1, T+1):
    dump = int(input())
    nums = list(map(int, input().split()))
    floors = [0] * 100
    # 해당 층 높이에 상자가 몇 개 있는지 체크
    for i in range(100):
        for num in nums:
            if num >= i+1:
                floors[i] += 1

    max_idx = 99
    min_idx = 0
    # 최고층에서 상자를 -1, 최저층에 상자를 +1
    while True:
        if max_idx == min_idx:
            # 평탄화가 완료되면 종료
            break

        if floors[max_idx] == 0:
            # 최고층에 상자가 없으면 한 층 내려감
            max_idx -= 1
            continue

        if floors[min_idx] == 100:
            # 최저층에 상자가 꽉 차면 한 층 올라감
            min_idx += 1
            continue

        if dump == 0:
            break

        if floors[max_idx] > 0:
            if floors[min_idx] < 100:
                floors[max_idx] -= 1
                floors[min_idx] += 1
                dump -= 1

    print(f'#{tc} {max_idx - min_idx + 1}')