import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


def is_digit(str):
    # 음수도 True로 리턴하는 함수
   try:
     tmp = int(str)
     return True
   except ValueError:
     return False

def calc_postfix(postfix_expression):
    '''
    후위표현식을 계산하여 결과를 리턴
    '''
    stack = []
    token = ''
    for char in postfix_expression:
        # 계산 종료
        if char == '.':
            if len(stack) != 1:
                return 'error'
            else:
                return stack.pop()
        # 공백일 때 n자리수 추가
        elif char != ' ':
            token += char
            continue

        elif char == ' ':
            if is_digit(token):
                stack.append(int(token))
            # 연산자라면 계산
            else:
                if len(stack) < 2:
                    return 'error'
                else:
                    num2 = int(stack.pop())
                    num1 = int(stack.pop())
                    if token == '+':
                        stack.append(num1 + num2)
                    elif token == '-':
                        stack.append(num1 - num2)
                    elif token == '*':
                        stack.append(num1 * num2)
                    elif token == '/':
                        stack.append(num1 // num2)
                    else:
                        return 'error'
            token = ''



T = int(input())
for tc in range(1, T+1):
    expression = input()
    ans = calc_postfix(expression)
    print(f'#{tc} {ans}')