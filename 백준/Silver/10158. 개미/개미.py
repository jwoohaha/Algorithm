# 가로, 세로
w, h = map(int, input().split())
# 초기 좌표
p, q = map(int, input().split())
# 시간
t = int(input())

# x 좌표가 감소하는 상태
if ((p+t) // w) % 2 == 1:
    x = w - (p+t) % w
# x 좌표가 증가하는 상태
else:
    x = (p+t) % w
# y 좌표가 감소하는 상태
if ((q+t) // h) % 2 == 1:
    y = h - (q+t) % h
# y 좌표가 증가하는 상태
else:
    y = (q+t) % h

print(x, y)