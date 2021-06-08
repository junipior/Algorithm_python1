# 6월 8일
# Greedy
# p.312

import sys
from collections import deque

num = list(map(int, sys.stdin.readline().rstrip()))
num = deque(num)
result = 1

while num:
    q = num.popleft()
    if q == 0:
        continue
    result *= q
print(result)

# 2번 째 방법
# data = input()
#
# # 첫 번째 문자를 숫자로 변환
# result = int(data[0])
#
# for i in range(data):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
#
# print(result)


# 02984 -> 576
# 567 -> 210