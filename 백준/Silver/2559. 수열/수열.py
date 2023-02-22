# 온도 측정 날짜 수, 연속적인 K일의 온도 합 출력
N, K = map(int, input().split())
temperatures = list(map(int, input().split()))
tmp = max_sum = sum(temperatures[:K])
front = 0
rear = K
# 가장 오래된 날 제외, 다음날 추가
for i in range(N-K):
    tmp = tmp - temperatures[front] + temperatures[rear]
    max_sum = max(max_sum, tmp)
    front += 1
    rear += 1
print(max_sum)