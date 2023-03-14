def dfs(idx, m, path):
    # 남은 수가 부족하면 리턴
    if N - idx < m:
        return
    nums = [num for num in range(1, N+1)]
    # 차례대로 수열에 추가
    for i in range(idx, N):
        dfs(i+1, m-1, path + [nums[i]])
    # 수열을 완성하면 결과에 추가
    if m == 0:
        result.append(path)


# main
N, M = map(int, (input().split()))
result = []
dfs(0, M, [])
for arr in result:
    print(*arr)