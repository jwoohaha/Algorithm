import sys
sys.stdin = open('input.txt', 'r')

# 암호화 코드
encryption = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}

hexa_dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def hex_to_bin(n):
    '''
    16진수를 2진수로 변환
    '''
    b = ''
    # 비트를 하나씩 이동하며 확인
    for i in range(4):
        if n & (1 << i):
            b = '1' + b
        else:
            b = '0' + b
    return b


def hex_to_bin_line(line):
    '''
    한 라인을 2진수로 변환
    '''
    result = ''
    for l in line:
        # 숫자라면 2진수로 변환한 숫자를 더해줌
        if l.isdigit():
            result += hex_to_bin(int(l))
        # 문자라면(10이상) dic 참조
        else:
            result += hex_to_bin(hexa_dic[l])
    return result


for T in range(int(input())):
    N, M = map(int, input().split())
    rstrip_data = set()
    codes = set()
    result = 0
    for _ in range(N):
        # 오른쪽 0들을 지워줌
        data = input().rstrip().rstrip('0')
        if data:
            # 2진수 변환 후 0 지워줌
            rstrip_data.add(hex_to_bin_line(data).rstrip('0'))
    for r in rstrip_data:
        r_data = r
        while len(r_data) > 0:
            k = 1  # 암호코드가 굵어진? 늘어난? 정도
            while len(r_data) - k * 56 >= 0:
                tmp = r_data[-56 * k:]
                # 늘어난 정도를 체크하는 문자열
                check1 = '0' + ('1' * k) + '0'
                check2 = '1' + ('0' * k) + '1'
                # k만큼 늘어나 있다면 break
                if check1 in tmp or check2 in tmp:
                    break
                else:
                    k += 1
            code = ''
            for _ in range(8):
                # 굵어진 암호코드를 처리
                last = ''
                raw_last = r_data[-7 * k:]
                for i in range(7):
                    last += raw_last[i * k]
                r_data = r_data[:-7 * k]
                code = encryption[last] + code
            codes.add(code)
            r_data = r_data.rstrip('0')

    # 유효한 코드인지 검증
    for code in codes:
        if ((int(code[0]) + int(code[2]) + int(code[4]) + int(code[6])) * 3 \
            + int(code[1]) + int(code[3]) + int(code[5]) + int(code[7])) % 10 == 0:
            result += sum(map(int, code))

    print(f'#{T + 1} {result}')
