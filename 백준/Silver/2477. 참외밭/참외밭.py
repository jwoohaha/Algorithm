# 오목한 부분은 연속해서 나타남
# ex) 3 1 3 1 (남 동 남 동)

K = int(input())
directions = []
lengths = []
for _ in range(6):
    direction, length = map(int, input().split())
    directions.append(direction)
    lengths.append(length)

set_directions = [1, 2, 3, 4]
d_directions = directions * 2
d_lengths = lengths * 2

for i in range(len(d_directions)):
    if d_directions[i:i+2] == d_directions[i+2:i+4]:
        set_directions.remove(d_directions[i+1])
        set_directions.remove(d_directions[i+2])
        minus_area = d_lengths[i+1] * d_lengths[i+2]
        break

long_lengths = []
for i in range(len(set_directions)):
    long_lengths.append(lengths[directions.index(set_directions[i])])

area = long_lengths[0] * long_lengths[1]
area -= minus_area
results = K * area
print(results)


