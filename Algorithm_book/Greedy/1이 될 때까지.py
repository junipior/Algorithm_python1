# 6월 8일
# Greedy
# p.99

import sys
count = 0
N, K = map(int, sys.stdin.readline().split())

while N >= K: # K로 나누는게 -1 하는 것보다 빠르게 숫자를 줄이는 방법에서 착안
    while N % K != 0: # K로 나눠지지 않을 때는 -1
        N -= 1
        count += 1
    N //= K # 나눠지면 N을 K로 나누고 몫을 N으로 재정의
    count += 1 # 결과 카운트 +1

if N == 2: # N이 2일 경우 -1
    N -= 1
    count += 1

print(count)

# input
# 25 5

# output
# 2