import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


def infix_to_postfix(infix):
    '''
    infix: 중위표기법으로 작성된 수식
    return: 후위표기법으로 변환된 수식
    '''
    stack = []
    result = ''

    # 변환할 식을 순회
    for token in infix:
        # 토큰이 피연산자인 경우
        if token.isdecimal():
            result += token

        # 토큰이 연산자인 경우
        else:
            # stack이 비어있는 경우, stack에 push
            if not stack:
                stack.append(token)

            # stack이 비어있지 않은 경우, 우선순위에 따라야겠다
            else:
                # incoming 우선순위가 2인 경우
                if token == '*':
                    # stack의 top의 토큰이 우선순위가 낮을 때까지 stack에서 pop, result에 append
                    while stack and stack[-1] == '*':
                        result += stack.pop()
                    stack.append(token)

                # incoming 우선순위가 1인 경우
                elif token == '+':
                    # stack의 top의 토큰이 우선순위가 낮을 때까지 stack pop, result에 append
                    # (가 아닌 경우 모두 동치
                    while stack and stack[-1] != '(':
                        result += stack.pop()
                    stack.append(token)

    while stack:
        result += stack.pop()

    return result

def calc_postfix(postfix_expression):
    '''
    후위표현식을 계산하여 결과를 리턴
    '''
    stack = []

    for token in postfix_expression:
        # 숫자라면 스택에
        if token.isdecimal():
            stack.append(token)
        # 연산자라면 계산
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if token == '+':
                stack.append(num1 + num2)
            elif token == '*':
                stack.append(num1 * num2)

    return stack[-1]


for tc in range(1, 11):
    garbage = input()
    infix = input()
    converted = infix_to_postfix(infix)
    ans = calc_postfix(converted)
    print(f'#{tc} {ans}')