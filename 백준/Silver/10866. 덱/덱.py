# deque
from collections import deque
from sys import stdin
N = int(stdin.readline())

deque = deque([])
for i in range(N):
    command = stdin.readline().split()
    if command[0] == 'push_front':
        deque.appendleft(command[1])
    
    elif command[0] == 'push_back':
        deque.append(command[1])

    elif command[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())

    elif command[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
        
    elif command[0] == 'size':
        print(len(deque))

    elif command[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])

    elif command[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])