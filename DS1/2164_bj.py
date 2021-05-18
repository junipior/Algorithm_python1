# 5월 18일
# 백준 2164
# 데크 이용

from collections import deque

deq = deque()

n = int(input())
for i in range(n):
    deq.append(i+1)

while len(deq) >= 3:
    deq.popleft()
    deq.append(deq.popleft())

if len(deq) == 2:
    deq.popleft()
    print(deq.pop())

if len(deq) == 1:
    print(deq.pop())
