import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


T = int(input())
for tc in range(1, T + 1):
    texts = input()
    ans = ['']
    # 중복 문자 지우기
    for char in texts:
        if ans[-1] == char:
            # 문자가 중복되면 pop
            ans.pop()
        else:
            # 중복이 아니라면 추가
            ans.append(char)

    print(f'#{tc} {len(ans) - 1}')