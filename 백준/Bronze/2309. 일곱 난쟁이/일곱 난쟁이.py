heights = []
for _ in range(9):
    heights.append(int(input()))

sum_heights = sum(heights)

for i in range(8):
    for j in range(i+1, 9):
        if sum_heights - heights[i] - heights[j] == 100:
            heights.pop(j)
            heights.pop(i)
            break
    if len(heights) == 7:
        break

heights.sort()
for height in heights:
    print(height)