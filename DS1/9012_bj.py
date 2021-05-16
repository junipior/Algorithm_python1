# 5월 16일
# 백준 9012
# 스택 이용

import sys

n = int(sys.stdin.readline()) # 읽어들인 문장중에 숫자만 변수로 저장
for _ in range(n): # 단순히 반복하는 경우 _ 사용
    stack = []
    vps = sys.stdin.readline().rstrip() # 우측 공백 없앰
    check = 0
    for c in vps[1:]:
        if c =='(': # 1. '('가 있을 경우 스택에 '('를 넣음
            stack.append(c)
        elif c ==')': # 2. ')'가 있을 경우 두가지로 나누어 생각
            if len(stack) == 0:  # 2-1. 스택의 길이가 0일경우 NO를 출력하고, check에 1을 대입
                print('')
                print('NO')
                check = 1
                break
            else:  # 2-2. 스택의 길이가 0이 아닐 경우 스택에 젤 우측(마지막)것을 뺌.
                stack.pop(-1)

    if len(stack) != 0 and check == 0:
        print('NO')
    elif len(stack) == 0 and check == 0:
        print('YES')


# input과 sys.stdin 차이 https://velog.io/@gouz7514/파이썬-input-vs-sys.stdin.readline