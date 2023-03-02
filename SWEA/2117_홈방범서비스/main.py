import sys
sys.stdin = open('input.txt', 'r')

'''
집을 기준으로 생각, 거리별로 집의 개수를 누적하여 구함
'''
def solve_idea():
    mx = 0
    home = []
    for si in range(N):
        for sj in range(N):  # [1] 집의 모든 위치를 저장
            if data[si][sj] == 1:
                home.append((si, sj))

    # [2] 각 기준위치에서 거리별 집의 개수 누적하기
    for si in range(N):
        for sj in range(N):  #
            dist = [0] * 40
            # 거리별 집위치를 누적
            for ti, tj in home:
                t = abs(si - ti) + abs(sj - tj) + 1
                dist[t] += 1

            for k in range(1, 40):
                dist[k] += dist[k - 1]
                if cost[k] <= dist[k] * M:
                    mx = max(mx, dist[k])
    return mx

'''
bfs로 풀이
모든 점을 돌면서 확산
집이 많으면 이 풀이가 더 좋을 수도 있으나 집이 적은 경우
집을 기준으로 생각하는 풀이가 더 빠름
'''
cost = [((k * k) + (k - 1) * (k - 1)) for k in range(40)]
def bfs(si, sj):
    # 시작 인덱스
    q = []
    # 방문 표시
    v = [[0] * N for _ in range(N)]
    # 이전 거리(k)
    old = 0
    mx = 0

    q.append((si, sj))
    v[si][sj] = 1
    cnt = data[si][sj]  # 시작좌표가 집이면 1, 아니면 0

    while q:
        ci, cj = q.pop(0)
        if old != v[ci][cj]:  # k값이 달라진경우
            old = v[ci][cj]
            if cost[v[ci][cj]] <= cnt * M:
                mx = max(mx, cnt)

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 유효한 인덱스이며 미방문한 점이면
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                q.append((ni, nj))
                # 거리 추가
                v[ni][nj] = v[ci][cj] + 1
                cnt += data[ni][nj]
    return mx


def solve_bfs():
    mx = 0
    for si in range(N):
        for sj in range(N):  # 가능한 모든 시작위치
            mx = max(mx, bfs(si, sj))
    return mx

T = int(input())
for tc in range(1, T+1):
    # 도시의 크기, 하나의 집이 지불할 수 있는 비용
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = solve_bfs()
    print(f'#{tc} {ans}')

# '''
# 브루트포스 풀이
# '''
# def check_coverage(k, row, col):
#     '''
#     k의 값에 따른 방범 서비스 제공 세대 수 리턴
#     '''
#     cnt = 0
#     # 가장 중앙 열 체크
#     for i in range(k * 2 - 1):
#         if -1 < row - k + 1 + i < N and -1 < col < N:
#             if data[row-k+1+i][col] == 1:
#                 cnt += 1
#     # 왼쪽 오른쪽 열을 하나씩 체크
#     for j in range(1, k):
#         for i in range((k - j) * 2 - 1):
#             # 오른쪽
#             if -1 < row - k + 1 + j + i < N and -1 < col + j < N:
#                 if data[row-k+1+j+i][col+j] == 1:
#                     cnt += 1
#             # 왼쪽
#             if -1 < row - k + 1 + j + i < N and -1 < col - j < N:
#                 if data[row-k+1+j+i][col-j] == 1:
#                     cnt += 1
#     return cnt
#
# T = int(input())
# for tc in range(1, T+1):
#     # 도시의 크기, 하나의 집이 지불할 수 있는 비용
#     N, M = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     # k의 범위를 줄여가며 서비스 가능한 최대 집의 수를 탐색
#     max_coverage = 0
#     for k in range(N+1, 0, -1):
#         for row in range(0, N):
#             for col in range(0, N):
#                 coverage = check_coverage(k, row, col)
#                 # 흑자
#                 if coverage * M >= 2*k*k - 2*k + 1:
#                     max_coverage = max(max_coverage, coverage)
#     print(f'#{tc} {max_coverage}')
