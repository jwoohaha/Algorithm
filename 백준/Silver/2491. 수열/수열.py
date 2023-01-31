# dp로 풀면 훨씬 쉽게 가능
num_length = int(input())
nums = list(map(int, input().split()))

# 수열 앞에서 부터 탐색하며
# 수 2개 비교 같으면 판단 유보
# 오름차순 처리
# 내림차순 처리
max_cnt = 0
cnt = 1
if num_length == 1:
    print(1)
else:
    for i in range(num_length-1):
        if nums[i] == nums[i+1]:  # 같으면 판단 유보
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt

        elif nums[i] < nums[i+1]:  # 오름차순
            cnt += 1
            for j in range(i+1, num_length-1):
                # 오름차순 유지하면 카운트 +1
                if nums[j] <= nums[j+1]:
                    cnt += 1
                else:  # 최대값 업데이트
                    break
            if cnt > max_cnt:
                max_cnt = cnt
            cnt = 1

        elif nums[i] > nums[i+1]:  # 내림차순
            cnt += 1
            for j in range(i+1, num_length-1):
                # 내림차순 유지하면 카운트 +1
                if nums[j] >= nums[j+1]:
                    cnt += 1
                else:  # 최대값 업데이트
                    break
            if cnt > max_cnt:
                max_cnt = cnt
            cnt = 1

    print(max_cnt)

