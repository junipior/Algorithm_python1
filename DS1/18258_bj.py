# 5월 17일
# 백준 18258
# 데크 사용하기

import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque()

for _ in range(n):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == "push":
        deq.append(int(command[1]))

    elif command[0] == "pop":
        if len(str(deq)) > 0:
            print(deq[0])
            deq = deq.popleft()
        else:
            print(-1)

    elif command[0] == "size":
        print(len(deq))

    elif command[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "front":
        if len(deq) != 0:
            print(deq[0])
        else:
            print(-1)

    elif command[0] == "back":
        if len(deq) != 0:
            print(deq[-1])
        else:
            print(-1)