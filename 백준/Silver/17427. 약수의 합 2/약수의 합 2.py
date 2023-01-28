n = int(input())
# 약수의 합의 합
sum_div = 0

for i in range(1, n+1):
    '''
    ex) 10 이하 수 중 2를 약수로 가진 수의 개수 5개 (n//i)
    '''
    sum_div += (n//i)*i

print(sum_div)

# 시간초과 (O(n^2))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         # brute force
#         if i % j == 0:
#             sum_div += j