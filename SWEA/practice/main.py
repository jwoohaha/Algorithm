import sys
sys.stdin = open('input.txt', 'r')


def rotate(magnet, dir):
    '''
    magnet을 방향에 맞게 회전
    return: None
    '''
    # 시계방향
    if dir == 1:
        magnet.insert(0, magnet.pop())
    # 반시계방향
    elif dir == 0:
        magnet.append(magnet.pop(0))


def score(magnets):
    ans = 0
    for i in range(1, 5):
        if magnets[i][0] == 1:
            ans += 2 ** (i-1)
    return ans


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    magnets.insert(0, 0)  # 인덱스 편의를 위한 dummy 삽입
    for _ in range(K):
        # 자석 번호, 회전 방향(1: 시계, -1: 반시계)
        m, dir = map(int, input().split())
        # 연결 상태 확인
        connections = [False, False, False]
        # 자석1, 2 연결 확인
        if magnets[1][2] != magnets[2][6]:
            connection1_2 = True
        # 자석2, 3 연결 확인
        if magnets[2][2] != magnets[3][6]:
            connection2_3 = True
        # 자석3, 4 연결 확인
        if magnets[3][2] != magnets[4][6]:
            connection3_4 = True

        # 자석 회전
        rotate(magnets[m], dir)

    print(f'#{tc} {score(magnets)}')
