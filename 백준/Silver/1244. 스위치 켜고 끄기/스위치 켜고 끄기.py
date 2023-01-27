# 인풋처리
switch_num = int(input())
switches = list(map(int, input().split()))
student_num = int(input())


def reverse_switch(idx):
    # 1인 스위치는 0, 0인 스위치는 1로
    if switches[idx] == 1:
        switches[idx] = 0

    elif switches[idx] == 0:
        switches[idx] = 1


for _ in range(student_num):
    sex, num = map(int, input().split())
    # 남학생 받은 수의 배수 스위치 상태 바꾸기
    if sex == 1:
        for i in range(switch_num): # i는 스위치
            if (i + 1) % num == 0: # i+1은 스위치 번호
                reverse_switch(i)

    if sex == 2:
        reverse_switch(num - 1)
        if num != 1 and num != switch_num:
            left_idx = num - 1
            right_idx = num + 1
            while left_idx >= 1 and right_idx <= switch_num:
                if switches[left_idx-1] == switches[right_idx-1]:
                    reverse_switch(left_idx-1)
                    reverse_switch(right_idx-1)
                    left_idx -= 1
                    right_idx += 1
                else:
                    break


cnt = 0
for i in range(switch_num):
    if cnt == 19:
        print(switches[i])
        cnt = 0
        continue
    print(switches[i], end=' ')
    cnt += 1
