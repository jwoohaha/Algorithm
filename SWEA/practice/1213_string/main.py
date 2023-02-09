import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


T = 10
for _ in range(T):
    tc = int(input())
    target_word = input()
    texts = input()
    M = len(target_word)
    cnt = 0

    for i in range(len(texts)-M+1):
        if texts[i:i+M] == target_word:
            cnt += 1

    print(f'#{tc} {cnt}')
