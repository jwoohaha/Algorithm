import sys
input = sys.stdin.readline


N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
# 끝나는 시간을 기준으로 정렬, 끝나는 시간이 같으면 시작 시간이 빠른 순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

end = meetings[0][1]  # 앞 미팅의 종료시간
cnt = 1

for i in range(1, N):
    # 앞 미팅과 겹치지 않으면 추가
    if meetings[i][0] >= end:
        end = meetings[i][1]
        cnt += 1

print(cnt)