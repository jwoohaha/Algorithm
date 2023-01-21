# 파이썬 리스트는 stable sort방식 (값이 같으면 기존 순서를 유지)
n = int(input())
members = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    members.append((age, name))

members.sort(key = lambda x : x[0])	# (age, name)에서 age만 비교

for member in members:
    print(member[0], member[1])