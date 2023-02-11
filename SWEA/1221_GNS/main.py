import sys
sys.stdin = open('input.txt', 'r')


num_sys = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX":6 , "SVN": 7, "EGT": 8, "NIN": 9}
T = int(input())
for tc in range(1, T+1):
    TC_NUM, N = map(str, input().split())
    texts = input().split()
    # num_sys에서 얻을 값을 기준으로 정렬
    texts.sort(key=lambda x: num_sys.get(x))


    print(TC_NUM)
    print(*texts)

