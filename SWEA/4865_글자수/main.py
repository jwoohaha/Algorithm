import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


T = int(input())
for tc in range(1, T+1):
    str1 = input()  # 비교해야 하는 글자들
    str2 = input()  # str2에 몇 개씩 들어있는지 찾기
    char_set = set(str1)
    max_cnt = 0

    for char1 in char_set:
        # str1의 글자를 꺼내서
        cnt = 0
        for char2 in str2:
            # str2에 몇 개씩 있는지 카운트 후 최대 값 찾기
            if char2 == char1:
                cnt += 1
        max_cnt = max(cnt, max_cnt)

    print(f'#{tc} {max_cnt}')
