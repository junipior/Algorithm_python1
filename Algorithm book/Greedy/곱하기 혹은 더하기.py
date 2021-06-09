# 6월 8일
# Greedy
# p.312

import sys
from collections import deque # deque 이용 이유. list.pop(0)은 시간 복잡도가 o(n)인데 popleft는 시간 복잡도가 o(1)임.

num = list(map(int, sys.stdin.readline().rstrip()))
num = deque(num)
result = 1

while num:
    q = num.popleft()
    if q == 0:
        continue # 0이면 아무것도 안함. 0을 더하나 아무것도 안하나 같아서.
    result *= q # 이 아니면 이전의 수와 곱함.
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