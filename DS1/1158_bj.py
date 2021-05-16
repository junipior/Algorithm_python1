# 5월 13일
# 백준 1158

from collections import deque

deq = deque()
ans = []
N, K = map(int, input().split()) # map 함수를 활용해 입력 받은 두변수를 띄어쓰기 기준으로 정수형으로 변환
for i in range(N):
    deq.append(i+1)

while len(deq) > 1:
    deq.rotate(-(K-1)) # ex) deque(['q', 'w', 'e', 'r', 't', 'y']), rotate(-2) -> deque(['e','r','t','y','q','w'])
    ans.append(deq[0])
    deq.popleft()

ans.append(deq[0])

print("<", end='')
for i in ans[:-1]:
    print(i, end=', ')
print(ans[-1], end='')
print('>')