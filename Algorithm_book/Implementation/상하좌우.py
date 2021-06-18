# 6월 17일
# Implementation
# p.110

# L : 왼쪽으로 한 칸 이동
# R : 오른쪽으로 한 칸 이동
# U : 위로 한 칸 이동
# D : 아래로 한 칸 이동

import sys
n = int(sys.stdin.readline())
cmd = sys.stdin.readline()

x = 1
y = 1

for i in cmd:
  if i == 'R':
    if y < 5:
      y += 1
  elif i == 'U':
    if x > 1:
      x -= 1
  elif i == 'D':
    if 5 > x:
      x += 1
  elif  i == 'L':
    if y > 1:
      y -= 1

print(x , y)

# input
# 5
# R R R U D D

# output
# 3 4


# # 문제 해설
# # N 입력받기
# n = int(input())
# x, y = 1, 1
# plans = input().split()
#
# # L, R, U, D에 따른 이동 방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
#
# # 이동 계획을 하나씩 확인
# for plan in plans:
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     # 이동 수행
#     x, y = nx, ny
#
# print(x, y)

