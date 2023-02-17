width, height = map(int, input().split())  # 가로, 세로
horizontal_line = [height]  # 가로선
vertical_line = [width]  # 세로선

N = int(input())  # 칼로 잘라야 하는 점선의 수

for _ in range(N):
    # 0은 가로, 1은 세로
    direction, num = map(int, input().split())
    if direction == 0:  # 가로선 추가
        horizontal_line.append(num)
    elif direction == 1:  # 세로선 추가
        vertical_line.append(num)
# 정렬 후 선들 사이의 차이를 구함
horizontal_line.sort(reverse=True)
vertical_line.sort(reverse=True)
# 다시 정렬하면 조각의 가로, 세로 길이가 정렬됨
for i in range(len(horizontal_line)-1):
    horizontal_line[i] -= horizontal_line[i+1]
horizontal_line.sort()
for i in range(len(vertical_line)-1):
    vertical_line[i] -= vertical_line[i+1]
vertical_line.sort()

print(horizontal_line[-1]*vertical_line[-1])