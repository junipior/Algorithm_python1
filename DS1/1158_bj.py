# 5월 12일
# 백준 1158

from collections import deque

def answer(y):
    queue = deque()
    for i in range(1, y+1):
        queue.append(i)
    print(queue)

answer(3)
