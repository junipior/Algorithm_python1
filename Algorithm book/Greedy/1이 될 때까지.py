# 6월 8일
# Greedy
# p.99

import sys
count = 0
N, K = map(int, sys.stdin.readline().split())

while N > K:
    while N % K != 0:
        N -= 1
        count += 1
    N //= K
    count += 1

while N > 1:
    N -= 1
    count += 1

print(count)
