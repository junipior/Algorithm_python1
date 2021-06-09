# 6월 9일
# Greedy
# p.311

import sys

n = int(sys.stdin.readline())

f = list(map(int, sys.stdin.readline().split()))

f.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수
for i in f: # 공포도가 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가 수 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹 수 증가 시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹수 출력

# input
# 5
# 2 3 1 2 2