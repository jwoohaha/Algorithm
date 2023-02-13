import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    print(f'#{tc}')

    if n == 1:
        print('1')

    elif n == 2:
        print('1')
        print('1 1')
    else:
        triangle = [[1], [1, 1]]
        # 파스칼 삼각형 만들어주기
        for i in range(1, n-1):
            row = [1]  # 처음 1
            # 전 행의 요소를 더해서 다음 행을 만들어줌
            for j in range(len(triangle[i])-1):
                row.append(triangle[i][j]+triangle[i][j+1])
            row.append(1)  # 마지막 1 추가
            triangle.append(row)
        # 출력
        for row in triangle:
            print(*row)
