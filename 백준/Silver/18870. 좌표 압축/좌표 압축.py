import sys
import bisect
input = sys.stdin.readline


# main
N = int(input())
data = list(map(int, input().split()))
# 중복 제거
num_set = set(data)
num = list(num_set)
num.sort()

results = []
for n in data:
    results.append(bisect.bisect_left(num, n))
print(*results)