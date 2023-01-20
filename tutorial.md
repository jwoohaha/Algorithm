# 파이썬 알고리즘 기초 다지기...

- 인풋처리
```python
a, b = map(int, input().split())
nums = list(map(int, input().split()))
```
- 조금 더 빠른 인풋처리
```python
import sys
sys.stdin.readline()

input() = sys.stdin.readline() # 소급적용 편리
```



- 조금 더 빠른 자료형\
deque의 경우 doubly linked list로 구현\
배열로 구현된 리스트와 비교했을 때 삽입, 삭제 연산에서 우위를 보임
```python
from collections import deque
```


- 파일 인풋으로 받기
```python
import sys
sys.stdin = open('filename')
```


- 리스트 생성
```python
default_nums = set([i for i in range(1, 10)])
```
- 2차원 리스트 생성

```python
2d_list = [[0]*9 for _ in range(9)]  # 9행 9열
```
- print
```python
print('hi', end='\n') 기본 / end='' 줄바꿈 없이
```
- try - catch 입력 에러가 들어왔을 때 동작 중단을 방지
```python
while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a + b)
```
- tuple로 묶어 list에 추가
- sort key 활용
```python
members.append((age, name))
# [(20, 'Sunyoung'), (21, 'Junkyu'), (21, 'Dohyun')]
members.sort(key = lambda x : x[0])	# (age, name)에서 age만 비교
```
```python

```
```python

```