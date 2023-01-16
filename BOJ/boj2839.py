# 설탕 배달
# 설탕 봉지는 5kg or 3kg만 존재
# 5,3kg 으로 조합 불가시 -1 출력

sugar = int(input())
bag = 0

# 5로 나눠질 때 까지 3으로 구성 -> 안되면 -1
while sugar >= 0:
    if sugar % 5 == 0:
        bag += sugar // 5
        print(bag)
        break
    sugar -= 3
    bag += 1

else:
    print(-1)