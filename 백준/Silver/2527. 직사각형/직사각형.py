for _ in range(4):
    nums = list(map(int, input().split()))
    # 가로 세로를 정수 집합으로
    # 가로가 1 ~ 3이면 {1, 2, 3}
    width_1 = set([i for i in range(nums[0], nums[2] + 1)])
    height_1 = set([i for i in range(nums[1], nums[3] + 1)])
    width_2 = set([i for i in range(nums[4], nums[6] + 1)])
    height_2 = set([i for i in range(nums[5], nums[7] + 1)])
    # 교집합 이용하여 가로 세로 겹치는 길이 구하기
    # 1이면 점 2 이상이면 선으로 만남
    width_overlap = len(width_1 & width_2)
    height_overlap = len(height_1 & height_2)
    # 공통부분 판별
    if width_overlap > 1 and height_overlap > 1:  # 면 * 면: 직사각형
        print('a')
    elif width_overlap == 1 and height_overlap > 1:  # 점 * 선분: 선분
        print('b')
    elif width_overlap > 1 and height_overlap == 1:  # 선분 * 점: 선분
        print('b')
    elif width_overlap == 1 and height_overlap == 1:  # 점 * 점: 점
        print('c')
    else:  # 안만남
        print('d')
