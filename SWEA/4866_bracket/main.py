import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


def parenthesis(texts):
    stk = []
    # 괄호 추가 및 검증
    for char in texts:
        # 여는 괄호면 추가
        if char == '{' or char == '(':
            stk.append(char)

        # 닫는 괄호일 때
        elif char == '}':
            # stk이 비어 있으면 0
            if not stk:
                return 0
            # 쌍이 맞으면 pop
            elif stk[-1] == '{':
                stk.pop()
            # 이외 0
            else:
                return 0

        elif char == ')':
            if not stk:
                return 0
            elif stk[-1] == '(':
                stk.pop()
            else:
                return 0
    # 다 돌고난 후
    if not stk:
        # stk이 비어 있으면 제대로 짝을 이룸
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    texts = input()
    print(f'#{tc} {parenthesis(texts)}')

