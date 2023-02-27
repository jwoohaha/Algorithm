import sys
sys.stdin = open('input.txt', 'r')

# 암호화 코드
encryption = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}


def cal_code(code):
    '''
    input[str]: 56자리 binary code
    return[int]: 자리수 합 or 0

    암호화 코드에 따라 값을 계산
    10의 배수일 경우 자리수 합 리턴
    10의 배수가 아니면 0 리턴
    '''
    lst = []
    # 7자리씩 끊어서 lst에 저장
    for i in range(8):
        tmp = code[i * 7:i * 7 + 7]
        lst.append(tmp)

    vals = []
    # 코드에 해당하는 십진수 값으로 변환
    for i in lst:
        if i in encryption:
            val = encryption[i]
            vals.append(val)
        # 이상한 코드라면 0 리턴
        else:
            return 0

    verification = 0
    # 규칙에 따라 확인 코드 계산
    for i in range(4):
        verification += vals[i * 2] * 3
        verification += vals[i * 2 + 1]
    # 확인 코드가 10의 배수면 각 자리의 수 합 리턴
    if verification % 10 == 0:
        return sum(vals)
    # 아니면 0 리턴
    return 0



T = int(input())
for tc in range(1, T+1):
    # 세로, 가로 배열
    N, M = map(int, (input().split()))
    data = []
    for _ in range(N):
        nums = input().rstrip('0')
        data.append(nums[-56:])
    for row in data:
        if row:
            code = row
            break

    print(f'#{tc} {cal_code(code)}')
