# 6월 8일
# Greedy
# p.92

import sys

sum = 0

N, M, K = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))

num = sorted(num) # 내림차순 정렬/ 오름차순 sorted(num, reverse = True), num.sort(reverse = True)

first = num[N-1] # 가장 큰 수
second = num[N-2] # 두 번 째로 큰 수
second_count = int(M//(K+1))
first_count = M - second_count

sum += (first * first_count) + (second * second_count)

print(sum)

