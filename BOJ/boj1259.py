# 팰린드롬수

while True:
    num = input()
    if num == '0':
        break
    if num == num[::-1]:  # num str을 역순으로
        print('yes')
    else:
        print('no')
