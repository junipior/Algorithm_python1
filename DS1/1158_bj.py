# 5월 13일
# 백준 1158

from collections import deque

deq = deque()
ans = []
N, K = map(int, input().split(' '))
for i in range(N):
    deq.append(i+1)

while len(deq) > 1:
    deq.rotate(-(K-1))
    ans.append(deq[0])
    deq.popleft()

ans.append(deq[0])

print("<", end='')
for i in ans[:-1]:
    print(i, end=', ')
print(ans[-1], end='')
print('>')


# 코드 참고 https://jinu0418.tistory.com/71
