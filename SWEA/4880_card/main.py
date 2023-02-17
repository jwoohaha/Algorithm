import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


def tournament(cards):
    '''
    토너먼트의 승자를 리턴(재귀)
    param: cards[List(tuple)]: 참가자들이 가진 카드의 정보(참가자번호, 카드종류)
    param: num_members[int]: 참가자 수
    return: tuple (승자번호, 카드종류)
    '''
    if len(cards) == 1:
        return [cards[0]]
    elif len(cards) == 2:
        # 비겼을 경우
        if cards[0][1] == cards[1][1]:
            return [cards[0]]
        # 가위, 바위
        elif cards[0][1] == 1 and cards[1][1] == 2:
            return [cards[1]]
        # 가위, 보
        elif cards[0][1] == 1 and cards[1][1] == 3:
            return [cards[0]]
        # 바위, 보
        elif cards[0][1] == 2 and cards[1][1] == 3:
            return [cards[1]]
        # 바위, 가위
        elif cards[0][1] == 2 and cards[1][1] == 1:
            return [cards[0]]
        # 보, 바위
        elif cards[0][1] == 3 and cards[1][1] == 2:
            return [cards[0]]
        # 보, 가위
        elif cards[0][1] == 3 and cards[1][1] == 1:
            return [cards[1]]
    else:
        # 재귀적으로 승자를 찾음
        if len(cards) % 2 == 1:
            partition = len(cards)//2 + 1
        else:
            partition = len(cards)//2
        left = tournament(cards[:partition])
        right = tournament(cards[partition:])
        return tournament(left + right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    cards = [(i+1, nums[i]) for i in range(N)]
    # 승자의 카드 번호를 리턴
    print(f'#{tc} {tournament(cards)[0][0]}')