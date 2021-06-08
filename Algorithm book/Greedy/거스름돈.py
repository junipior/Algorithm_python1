# 6월 8일
# Greedy
# p.87

import sys

N = int(sys.stdin.readline())

coin_types = [500, 100, 50, 10]

count = 0 # 필요한 동전 수 세기위한 count 변수 초기화

for coin in coin_types:
    count += N // coin
    N %= coin

print(count)