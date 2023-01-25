N = int(input())
dots = []

for n in range(N):
    dot = list(map(int, input().split()))
    dots.append(dot)
# x, y 좌표 순으로 정렬
dots.sort(key = lambda x: (x[0], x[1]))

for dot in dots:
    print(dot[0], dot[1])