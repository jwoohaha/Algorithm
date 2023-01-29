'''
이후 구간 최대가 아니면 최대를 만날 때 까지 현재 최대 유지
최대면 남은 구간 중 최대 높이로 (오목한 부분이 없어야 함)
'''
from sys import stdin
input = stdin.readline

N = int(input())  # 기둥의 개수
pillars = [0] * 1001  # 기둥의 위치
for n in range(N):
    # 기둥의 위치, 높이
    idx, height = map(int, input().split())
    pillars[idx] = height

tmp_max = 0
area = 0
for i in range(1001):
    if pillars[i] > tmp_max:
        tmp_max = pillars[i]

    if tmp_max >= max(pillars[i:]):
        # 현재 기둥 높이가 이후 구간 최대인 경우
        area += tmp_max
        if i < 1000:
            # 남은 구간 중 최대 높이로 짓기
            tmp_max = max(pillars[i+1:])
        continue

    area += tmp_max

print(area)

