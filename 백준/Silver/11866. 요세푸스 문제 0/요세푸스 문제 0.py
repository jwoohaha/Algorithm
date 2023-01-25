from collections import deque # popleft 연산에 list와 비교하여 훨씬 유리

N, K = map(int, input().split())
queue = deque([num for num in range(1, N+1)])
order = []

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft()) # k-1번 큐의 맨 앞 요소를 뒤로 보냄
    order.append(queue.popleft())

print('<', end='')
print(', '.join(map(str, order)), end='')
print('>')