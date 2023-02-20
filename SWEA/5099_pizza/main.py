import sys
from collections import deque
sys.stdin = open('input.txt', 'r', encoding='utf-8')


def bake_pizza(pizzas, pot):
    while len(pot) > 1:
        # 치즈의 반감기
        pot[0][1] //= 2
        # 치즈가 다 녹으면 빼주기
        if pot[0][1] == 0:
            pot.pop(0)
            # 남은 피자가 있으면 넣어주기
            if pizzas:
                pot.append(pizzas.pop(0))
        # 다 안녹았으면 큐의 맨 뒤로
        else:
            pot.append(pot.pop(0))

    return pot.pop()[0] + 1


T = int(input())
for tc in range(1, T+1):
    pizzas = []  # 피자 정보
    pot = []  # 화덕
    # 화덕의 크기, 피자 개수
    N, M = map(int, input().split())
    # 치즈의 양
    data = list(map(int, input().split()))
    # 리스트 형태로 저장
    for i, c in enumerate(data):
        pizzas.append([i, c])
    # 초기 세팅(화덕)
    for i in range(N):
        pot.append(pizzas.pop(0))

    print(f'#{tc} {bake_pizza(pizzas, pot)}')
