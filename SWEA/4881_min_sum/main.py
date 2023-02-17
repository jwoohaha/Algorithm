import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


def min_sum(idx, cnt):
    '''
    열을 돌며 하나 씩 선택
    행을 내려가 반복
    이미 최소값을 넘으면 가지치기
    '''
    global result

    # 가지치기
    if cnt >= result:
        return

    # 모든 행 고려 후 최솟값 업데이트
    if idx == N:
        if result > cnt:
            result = cnt
        return

    # 조사
    for j in range(N):  # 열
        if selected[j] == 0:
            # 선택
            selected[j] = 1
            # 다음 행으로
            min_sum(idx+1, cnt+data[idx][j])
            # 해당 가지 탐색 후 선택 초기화
            selected[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 결과값
    result = 0
    for i in range(N):
        result += sum(data[i])

    # 선택 여부 확인용 리스트(열 중복 방지)
    selected = [0] * N

    # 현재 조사 위치, 종합
    min_sum(0, 0)
    print(f'#{tc} {result}')
