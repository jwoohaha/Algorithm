import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')

'''
0열역순 2행역순 2열
1열역순 1행역순 1열
2열역순 0행역순 0열 
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())  # N * N 행렬
    in_matrix = [list(map(str, input().split())) for _ in range(N)]
    r_matrix = [[''] * 3 for _ in range(N)]

    for i in range(N):
        # r_matrix 0열
        for k in range(N):
            r_matrix[i][0] += in_matrix[N-1-k][i]  # 회전된 결과 0열 = i열 역순
            r_matrix[i][1] += in_matrix[N-1-i][N-1-k]  # 회전된 결과 1열 = N-1-i행 역순
            r_matrix[i][2] += in_matrix[k][N-1-i]  # 회전된 결과 2열 = N-1-i열

    print(f'#{tc}')
    for i in range(N):
        print(' '.join(r_matrix[i]))

