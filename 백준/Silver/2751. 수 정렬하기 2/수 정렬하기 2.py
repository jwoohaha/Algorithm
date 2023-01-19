import sys


nums = []
N = int(sys.stdin.readline())
for i in range(N):
    nums.append(int(sys.stdin.readline()))
nums.sort()
for num in nums:
    print(num)