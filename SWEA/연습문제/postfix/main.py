# import sys
# sys.stdin = open('input.txt', 'r', encoding='utf-8')


# in-coming priority
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
# in-stack priority
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

def postfix(infix):
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
                # (는 incoming 우선순위가 가장 높음
                if token == '(':
                    stack.append(token)
                # )는 (가 나올때까지 stack에서 pop, result에 append
                elif token == ')':
                    while stack[-1] != '(':
                        result += stack.pop()
                    # (가 나오면 그냥 버리기
                    stack.pop()

                # incoming 우선순위가 2인 경우
                elif token == '*' or token == '/':
                    # stack의 top의 토큰이 우선순위가 낮을 때까지 stack에서 pop, result에 append
                    while stack and stack[-1] == '*' or stack[-1] == '/':
                        result += stack.pop()
                    stack.append(token)

                # incoming 우선순위가 1인 경우
                elif token == '+' or token == '-':
                    # stack의 top의 토큰이 우선순위가 낮을 때까지 stack pop, result에 append
                    # (가 아닌 경우 모두 동치
                    while stack and stack[-1] != '(':
                        result += stack.pop()
                    stack.append(token)

    while stack:
        result += stack.pop()

    return result

str = '(6+5*(2-8)/2)'
print(postfix(str))