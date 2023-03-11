import sys
input = sys.stdin.readline

M = int(input())  # 연산의 수
S = set()

for _ in range(M):
    tmp = input().split()

    if len(tmp) == 1:
        if tmp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()

    else:
        op, x = tmp[0], tmp[1]
        x = int(x)

        if op == "add":
            S.add(x)
        elif op == "remove":
            S.discard(x)
        elif op == "check":
            print(1 if x in S else 0)
        elif op == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
